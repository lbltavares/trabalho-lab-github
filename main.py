from queries import queries
import requests as req
import json
import csv
import os

BASE_URL = "https://api.github.com/graphql"

# Token do GitHub:
# https://docs.github.com/pt/github/authenticating-to-github/creating-a-personal-access-token
GH_TOKEN = os.environ["GH_TOKEN"]

# Caminho dos arquivos .CSV:
CAMINHO_CSV = "csv/"

# Numero de repositorios a serem coletados para responder cada questao:
NUMERO_REPOSITORIOS = 1000


def post(query, cursor="null"):
    # Realiza uma solicitacao para a API GraphQL
    try:
        res = req.post(BASE_URL,
                       json={"query": query % cursor, "variables": {}},
                       headers={"Authorization": "Bearer " + str(GH_TOKEN)})
        if res.status_code != 200 or not res.json()["data"]["search"]:
            raise Exception("Status Code Invalido: " + str(res))
        return res.json()
    except Exception as e:
        return None


def criar_csv(nome, rows):
    # Escreve os repositorios coletados em um arquivo .CSV
    try:
        with open(nome, 'w') as f:
            w = csv.DictWriter(f, rows[0].keys())
            w.writeheader()
            w.writerows(rows)
    except Exception as e:
        print(e)


def main():
    for q in queries:
        repos = []
        cursor = "null"
        print("Questao #%d" % q["questao"])
        pagina = 0
        while len(repos) < NUMERO_REPOSITORIOS:
            res = None
            while not res:  # Tenta fazer uma nova requisicao em caso de falha
                res = post(q["query"], cursor)
            pagina += 1
            print("  pagina %d" % pagina)
            pageInfo = res["data"]["search"]["pageInfo"]
            repos.extend(res["data"]["search"]["nodes"])
            if pageInfo["hasNextPage"]:
                cursor = "\"%s\"" % pageInfo["endCursor"]
            else:
                break
        criar_csv("%squestao%d.csv" % (CAMINHO_CSV, q["questao"]), repos)


if __name__ == "__main__":
    main()

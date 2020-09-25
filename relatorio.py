# coding: utf-8

import csv
import json
import datetime
import dateutil
import numpy as np
import statistics as stat
from collections import Counter
import matplotlib.pyplot as plt

hoje = dateutil.parser.parse("2020-09-16T12:00:00Z")
lingPopulares = ["JavaScript", "HTML", "CSS", "SQL",
                 "Python", "Java", "Bash", "Shell",
                 "C#", "PHP", "C++", "TypeScript", "C",
                 "Ruby", "Go", "Assembly", "Swift", "Kotlin",
                 "R", "VBA", "Objective-C", "Scala", "Rust",
                 "Dart", "Elixir", "Clojure", "WebAssembly"]


# Converte as linhas de um arquivo CSV para dicts
def lerCSV(file):
    reader = csv.DictReader(open(file))
    for row in reader:
        for attr in row:
            try:  # Tenta converter o atributo de json para um objeto
                objAttr = json.loads(row[attr].replace("'", '"'))
                row[attr] = objAttr
            except ValueError:
                pass
        yield row


# Sistemas populares são maduros/antigos?
# Métrica: idade do repositório (calculado a partir da data de sua criação)
def RQ1():
    print("=== RQ1 ===")
    idades = [(hoje - dateutil.parser.parse(r["createdAt"])).days / 365
              for r in lerCSV("csv/questao1.csv")]
    print("Repositórios analisados: %d" % len(idades))
    print("Média: %.1f anos" % stat.mean(idades))
    print("Mediana: %.1f anos" % stat.median(idades))
    print("Desvio-Padrão: %.1f anos" % stat.stdev(idades))
    # Mostra o histograma das idades
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(idades, bins=50)
    plt.gca().set(title='RQ1. Idades de repositórios mais populares',
                  ylabel='Frequência', xlabel="Idade (em anos)")
    plt.show()


# Sistemas populares recebem muita contribuição externa?
# Métrica: total de pull requests aceitas
def RQ2():
    print("=== RQ2 ===")
    prAceitas = [r["pullRequests"]["totalCount"]
                 for r in lerCSV("csv/questao2.csv")]
    print("Repositórios analisados: %d" % len(prAceitas))
    print("Média: %.1f pull-requests aceitas" % stat.mean(prAceitas))
    print("Mediana: %.1f pull-requests aceitas" % stat.median(prAceitas))
    print("Desvio-Padrão: %.1f pull-requests aceitas" % stat.stdev(prAceitas))
    # Mostra o histograma das pull requests aceitas
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(prAceitas, bins=50)
    plt.gca().set(title='RQ2. Contribuição externa em repositórios mais populares',
                  ylabel='Frequência', xlabel="Pull-Requests Aceitas")
    plt.show()


# Sistemas populares lançam releases com frequência?
# Métrica: total de releases
def RQ3():
    print("=== RQ3 ===")
    releases = [r["releases"]
                for r in lerCSV("csv/questao3.csv")
                if r["releases"]["totalCount"] > 0]  # Desconsidera os que nao possuem releases

    print("* Análise de quantidade de releases:")
    totalPorRepo = [r["totalCount"] for r in releases]
    print("Repositórios analisados: %d" % len(totalPorRepo))
    print("Média: %.1f releases" % stat.mean(totalPorRepo))
    print("Mediana: %.1f releases" % stat.median(totalPorRepo))
    print("Desvio-Padrão: %.1f releases" % stat.stdev(totalPorRepo))
    print("* Análise do tempo entre releases:")
    releasesPorRepo = [r["nodes"] for r in releases if r["totalCount"] > 1]
    tempoEntreReleases = []
    for rel in releasesPorRepo:
        rel = sorted([dateutil.parser.parse(r["createdAt"]) for r in rel])
        tmp = []
        for i in range(0, len(rel) - 1):
            if rel[i] > rel[i+1]:
                print("asd")
            tmp.append((rel[i+1] - rel[i]).days)
        tempoEntreReleases.append(stat.mean(tmp))
    print("Repositórios analisados: %d" % len(tempoEntreReleases))
    print("Média: %.1f dias" % stat.mean(tempoEntreReleases))
    print("Mediana: %.1f dias" % stat.median(tempoEntreReleases))
    print("Desvio-Padrão: %.1f dias" % stat.stdev(tempoEntreReleases))
    # Mostra o histograma dos releases
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(totalPorRepo, bins=50)
    plt.gca().set(title='RQ3. Sistemas populares lançam releases com frequência?',
                  ylabel='Frequência', xlabel="Total de Releases")
    plt.show()
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(tempoEntreReleases, bins=50)
    plt.gca().set(title='RQ3. Sistemas populares lançam releases com frequência?',
                  ylabel='Frequência', xlabel="Tempo entre Releases (em dias)")
    plt.show()


# Sistemas populares são atualizados com frequência?
# Métrica: tempo até a última atualização (calculado a partir da data de última atualização)
def RQ4():
    print("=== RQ4 ===")
    tempos = [(hoje - dateutil.parser.parse(r["updatedAt"])).days
              for r in lerCSV("csv/questao4.csv")]
    print("Repositórios analisados: %d" % len(tempos))
    print("Média: %.1f horas" % (stat.mean(tempos) * 24))
    print("Mediana: %.1f horas" % (stat.median(tempos) * 24))
    print("Desvio-Padrão: %.1f horas" % (stat.stdev(tempos) * 24))
    # Mostra o histograma
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(tempos, bins=50)
    plt.gca().set(title='RQ4. Atualização de repositórios mais populares',
                  ylabel='Frequência', xlabel="Tempo desde a última atualização (em dias)")
    plt.show()


# Sistemas populares são escritos nas linguagens mais populares?
# Métrica: linguagem primária de cada um desses repositórios
def RQ5():
    linguagens = [l["languages"]["edges"][0]["node"]["name"]
                  for l in lerCSV("csv/questao5.csv")
                  if len(l["languages"]["edges"]) > 0]

    # Conta as 25 primeiras frequências e ordena os resultados
    # OBS: O numero 25 foi escolhido pois é a mesma quantidade
    # de linguagens exibidas na lista do StackOverflow
    langList = Counter(linguagens).most_common()
    counts = langList[:25]
    outras = langList[25:]
    counts.append(("Outras", sum([o[1] for o in outras])))

    lingPresentes = [l[0] for l in langList if l[0] in lingPopulares]
    percLing = (len(lingPresentes)/len(lingPopulares)) * 100
    print("%.2f%% Linguagens presentes" % percLing)

    total = sum([i[1] for i in langList])
    totalLingPopulares = sum(i[1] for i in langList if i[0] in lingPopulares)
    percRepos = (totalLingPopulares/total) * 100
    print("%.2f%% Repositórios escritos em linguagens populares" % percRepos)

    # Total de repositorios
    print("Total:")
    print(total)

    # Distribuição de Frequência
    plt.rcdefaults()
    fig, ax = plt.subplots()
    langNames = [l[0] for l in counts]
    y_pos = np.arange(len(langNames))
    langFreqs = [l[1] for l in counts]
    right_side = ax.spines["right"].set_visible(False)
    right_side = ax.spines["left"].set_visible(False)
    right_side = ax.spines["top"].set_visible(False)
    for i, v in enumerate(langFreqs):
        ax.text(v + 3, i + .25, str(v), color="black")
    ax.set_title("RQ5. Linguagens em repositórios mais populares")
    ax.set_xlabel("Frequência")
    ax.barh(y_pos, langFreqs, align="center")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(langNames)
    ax.invert_yaxis()
    plt.subplots_adjust(left=0.215)
    plt.show()


# Sistemas populares possuem um alto percentual de issues fechadas?
# Métrica: razão entre número de issues fechadas pelo total de issues
def RQ6():
    print("=== RQ6 ===")
    repos = [(r["closedIssues"]["totalCount"] / r["totalIssues"]["totalCount"]) * 100
             for r in lerCSV("csv/questao6.csv")
             if r["totalIssues"]["totalCount"] > 0]
    print("Repositórios analisados: %d" % len(repos))
    print("Média: %.1f%% issues fechadas" % (stat.mean(repos)))
    print("Mediana: %.1f%% issues fechadas" % (stat.median(repos)))
    print("Desvio-Padrão: %.1f%% issues fechadas" % (stat.stdev(repos)))
    # Mostra o histograma
    plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 100})
    plt.hist(repos, bins=50)
    plt.gca().set(title='RQ6. Sistemas populares possuem um alto percentual de issues fechadas?',
                  ylabel='Frequência', xlabel="% de Issues fechadas")
    plt.show()


# Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?
# Dica: compare os resultados para os sistemas com as linguagens da reportagem com os resultados de sistemas em outras linguagens.
def RQ7():
    print("=== RQ7 ===")
    hoje = dateutil.parser.parse("2020-09-25T20:00:00Z")

    repos1 = [r for r in lerCSV("csv/questao7.csv")
              if len(r["languages"]["edges"]) > 0
              and r["languages"]["edges"][0]["node"]["name"] not in lingPopulares]
    repos2 = [r for r in lerCSV("csv/questao7.csv")
              if len(r["languages"]["edges"]) > 0
              and r["languages"]["edges"][0]["node"]["name"] in lingPopulares][:len(repos1)]
    # Pull-Requests Aceitas
    print("Repos1 = Outras Linguagens")
    print("Repos2 = Linguagens Populares")
    print("Contribuição Externa:")
    print("Repos1: %.2f" % (stat.median([r["pullRequests"]["totalCount"]
                                         for r in repos1])))
    print("Repos2: %.2f" % (stat.median([r["pullRequests"]["totalCount"]
                                         for r in repos2])))
    # Numero de Releases
    print("Número de Releases:")
    print("Repos1: %.2f" % (stat.median([r["releases"]["totalCount"]
                                         for r in repos1
                                         if r["releases"]["totalCount"] > 0])))
    print("Repos2: %.2f" % (stat.median([r["releases"]["totalCount"]
                                         for r in repos2
                                         if r["releases"]["totalCount"] > 0])))
    # Último Update
    print("Tempo desde a última atualização:")
    print("Repos1: %.2f" % (stat.median([((hoje - dateutil.parser.parse(r["updatedAt"])).seconds / 60) / 60
                                         for r in repos1])))
    print("Repos2: %.2f" % (stat.median([((hoje - dateutil.parser.parse(r["updatedAt"])).seconds / 60) / 60
                                         for r in repos2])))


if __name__ == "__main__":
    RQ1()
    RQ2()
    RQ3()
    RQ4()
    RQ5()
    RQ6()
    RQ7()

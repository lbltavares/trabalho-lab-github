# coding: utf-8

import csv
import json
import datetime
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


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
    
    pass


# Sistemas populares recebem muita contribuição externa?
# Métrica: total de pull requests aceitas
def RQ2():
    pass


# Sistemas populares lançam releases com frequência?
# Métrica: total de releases
def RQ3():
    pass


# Sistemas populares são atualizados com frequência?
# Métrica: tempo até a última atualização (calculado a partir da data de última atualização)
def RQ4():
    pass


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
    pass


# Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?
# Dica: compare os resultados para os sistemas com as linguagens da reportagem com os resultados de sistemas em outras linguagens.
def RQ7():
    pass


RQ1()
# RQ2()
# RQ3()
# RQ4()
# RQ5()
# RQ6()
# RQ7()

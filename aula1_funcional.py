import pandas as pd

dados = pd.read_csv('feedbacks.csv', delimiter= ';')

notas = dados['nota']


def calcularNps(notas):
    detratores = notas.apply(lambda nota: nota <= 6).sum()
    promotores = notas[notas >= 9].count()
    
    return (promotores - detratores) / len(notas) * 100

nps = calcularNps(notas)
print(nps)



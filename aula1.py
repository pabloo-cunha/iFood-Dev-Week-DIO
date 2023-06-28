import pandas as pd 

dados = pd.read_csv('feedbacks.csv', delimiter = ';')

detratores = 0
promotores = 0

notas = dados['nota']

for x in notas:
    if x >= 9:
        promotores += 1
    elif x <= 6:
        detratores += 1
        
nps = (promotores - detratores) / len(notas) * 100

print(nps)
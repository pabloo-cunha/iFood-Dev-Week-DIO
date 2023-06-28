import gdown
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# file_id = '1eT-_sOIUzJxhJYt2JMrhTGDxCtOvW9Qf/view?usp=drive_link'
# gdown.download(f'https://drive.google.com/uc?id={file_id}', 'feedbacks.csv')

class Feedback:
    def __init__(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario

class AnaliseFeedback:
    def __init__(self, feedbacks):
        self.feedbacks = feedbacks

    def calcularNps(self):
        detratores = sum([1 for x in self.feedbacks if x.nota <= 6])
        promotores = sum([1 for x in self.feedbacks if x.nota >= 9])
        
        nps = (promotores - detratores) / len(self.feedbacks) * 100
        return nps

dados = pd.read_csv('feedbacks.csv', delimiter= ';')

# feedbacks = [Feedback(linha['nota'], linha['comentario'])  for indice, linha in dados.iterrows()]
feedbacks = dados.apply(lambda linha: Feedback(linha['nota'], linha['comentario']), axis=1)

analisador = AnaliseFeedback(feedbacks)

nps = analisador.calcularNps()

# Definição das constantes que usaremos para visualizar o NPS
NPS_ZONAS =   ['Crítico', 'Aperfeiçoamento', 'Qualidade', 'Excelência']
NPS_VALORES = [-100, 0, 50, 75, 100]
NPS_CORES =   ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']

# TODO: Criar um gráfico usando "matplotlib" para visualizar o NPS que calculamos no Dia 1!

def criar_grafico_nps(nps):
    fig, ax = plt.subplots(figsize = (10,2))
    
    for i, zona in enumerate(NPS_ZONAS):
        ax.barh([0], width=NPS_VALORES[i+1] - NPS_VALORES[i], left=NPS_VALORES[i], color = NPS_CORES[i])
    
    ax.barh([0], width=1, left=nps, color = 'black')
    ax.set_yticks([])
    ax.set_xlim(-100, 100)
    ax.set_xticks(NPS_VALORES)
    
    plt.text(nps, 0, f'{nps:.2f}', ha='center', va= 'center', color = 'white', bbox = dict(facecolor='000000'))
    
    patches = [mpatches.Patch(color=NPS_CORES[i], label=NPS_ZONAS[i]) for i in range(len(NPS_ZONAS))]
    plt.legend(handles = patches, bbox_to_anchor= (1,1))
    
    plt.title('Gráfico de NPS da iFood Dev Week')
        
        
    plt.show()
    

criar_grafico_nps(nps)
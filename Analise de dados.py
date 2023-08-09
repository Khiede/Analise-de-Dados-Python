import pandas as pd
import plotly.express as px
from IPython.display import display

#Visualizando os dados da tabela
tabela = pd.read_csv("C:/Users/KELVIN/Desktop/Analise de Dados com Python/cancelamentos.csv")
display(tabela)
display(tabela.info)

#Após a verificação dos dados, retirei valores vazios e a coluna "CustomerID"(Pois ela não será necessária)
tabela = tabela.dropna()
tabela = tabela.drop("CustomerID", axis=1)

#Verificando a porcentagem de cancelamentos utilizando todos os dados
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

"""Após uma análise completa dos dados por meio dos gráficos gerados, identifiquei que as maiores causas
de cancelamento são:
*Clientes com assinatura Mensal;
*Clientes acima dos 50 anos;
*Clientes com a conta em atraso por 21 dias ou mais;
*Clientes que ligam mais do que 5 vezes ao Call Center
Então realizei a checagem de cancelamentos sem esses dados.
"""
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["idade"]<=50]
tabela = tabela[tabela["dias_atraso"]<=20]
tabela = tabela[tabela["ligacoes_callcenter"]<=5]

display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

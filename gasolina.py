import pandas as pd
import seaborn as sns

data = pd.read_csv("gasolina.csv")
grafico = sns.lineplot(data=data,x="dia",y="venda",palette="pastel")
grafico.figure.savefig("gasolina.png")
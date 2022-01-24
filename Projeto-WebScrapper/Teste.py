import pandas as pd
import re

filename = 'Scrapper 6_1.csv'
pat = re.compile(r'^[^a-zA-Z]+|[\"*?\[\'R$]|[\'\]\"]')  # regex pra selecionar os valores da str a ser trocado
repl = ["", "."]
fieldnames = ['Nome', 'Precos']
df1 = pd.read_csv(filename, encoding='latin-1')
df1 = df1.replace([pat, r","], repl, regex=True)
nome = df1['Nome'].tolist()
preco = df1['Precos'].tolist()


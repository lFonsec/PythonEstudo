import datetime
import re
import pandas as pd


data = datetime.datetime.now()
checaDia = data.day
checaMes = data.month
diaMes = str(checaDia) + "_" + str(checaMes) + ".csv"
filename = "Scrapper " + diaMes
df1 = pd.read_csv(filename, encoding='latin-1')
df2 = pd.read_csv('Scrapper Pao de Ac ' + diaMes, encoding='latin-1')

pat = re.compile(r'^[^a-zA-Z]+|[\"*?\[\'R$]|[\'\]\"]')  # regex pra selecionar os valores da str a ser trocado
check = re.compile(r'^CERVEJA')
repl = ["", "."]
fieldnames = ['Nome', 'Precos']
df1 = df1.replace([pat, r","], repl, regex=True)
df2 = df2.replace([pat, r","], repl, regex=True)

df1['Nome'] = df1['Nome'].str.upper()
df1 = df1.sort_values('Nome')
df2['Nome'] = df2['Nome'].str.upper()
df2 = df2.sort_values('Nome')

df1["Precos"] = round(df1["Precos"].astype(float), 2)
df2["Precos"] = round(df2["Precos"].astype(float), 2)

df1 = df1[df1["Nome"].str.contains(check)]
df2 = df2[df2["Nome"].str.contains(check)]

df1.to_csv(path_or_buf=f"ADG_DTB {data.day}_{data.month}.csv", header=fieldnames, index=False)
df2.to_csv(path_or_buf=f"PDA_DTB {data.day}_{data.month}.csv", header=fieldnames, index=False)

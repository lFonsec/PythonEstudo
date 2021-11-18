import datetime
import re
import pandas as pd


data = datetime.datetime.now()
checaDia = data.day
checaMes = data.month
filename = "Scrapper " + str(checaDia) + "_" + str(checaMes) + ".csv"
df1 = pd.read_csv(filename, encoding='latin-1')

if checaDia == 1:
    if checaMes == 3:  # Checa se o mes vai ser fev
        checaDia = 28
        checaMes = data.month - 1
    elif checaMes == 12 or 10 or 7 or 5:  # Checa se o mes vai ser nov, set, jun ou abr
        checaDia = 30
        checaMes = data.month - 1
    else:  # Checa se o mes vai ser jan, mar, mai, jul, ago, out
        checaDia = 31
        checaMes = data.month-1
else:
    checaDia = checaDia - 1

filename2 = "Scrapper " + str(checaDia) + "_" + str(checaMes) + ".csv"
df2 = pd.read_csv(filename2, encoding='latin-1')
pat = re.compile(r'\[\'R?\$?')  # começo
pat2 = re.compile(r'\'\]')  # fim
repl = ["", "", "."]
fieldnames = ['Nome', 'Precos']
df1 = df1.replace([pat, pat2, r","], repl, regex=True)
df2 = df2.replace([pat, pat2, r","], repl, regex=True)
df1["Precos"] = df1["Precos"].astype(float)
df2["Precos"] = df2["Precos"].astype(float)
df1.sort_values('Nome')
df2.sort_values('Nome')
df1["Precos"] = df1["Precos"].sub(df2["Precos"])
df1 = df1[df1["Precos"] != 0.0]

df1.to_csv(path_or_buf=f"Pandas {data.day}_{data.month}.csv", header=fieldnames)

"""
1 Jan = 31 
2 Fev = 28
3 Mar = 31
4 Abr = 30 
5 Mai = 31
6 Jun = 30
7 Jul = 31
8 Ago = 31
9 Set = 30
10 Out = 31
11 Nov = 30
12 Dez = 31
"""

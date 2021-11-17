import datetime
import re

import pandas as pd


data = datetime.datetime.now()
checaDia = data.day
checaMes = data.month
filename = "Scrapper " + str(checaDia) + "_" + str(checaMes) + ".csv"
df1 = pd.read_csv(filename, encoding='latin-1')
print(df1)

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
print("----------------------------------------")
pat = re.compile(r'\[\]\"\'')
pd.Series(df1).str.replace(pat, "", regex=True)


# df1['Precos'] = df1['Precos'].astype(int)
# df3 = df1.sub(df2)

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

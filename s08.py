import random
import math
""""
# 1)

def quadrado(numero):
    return numero ** 2


numero = int(input("digite o valor que quer dobrar: "))
print(f'o valor é: {quadrado(numero)}')
"""

#  2)
"""

def data(mes):
    switch = {
        '1': 'janeiro',
        '2': 'fevereiro',
        '3': 'marco',
        '4': 'abril',
        '5': 'maio',
        '6': 'junho',
        '7': 'julho',
        '8': 'agosto',
        '9': 'setemro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }
    return switch.get(mes)


dia = input("digite o dia: ")
mes = input("digite o mes: ")
ano = input("digite o ano: ")
aux = data(mes)
print(f'a data é: {dia} de {aux} de {ano}')
"""

#  3)

"""
def checa_valor(valor):
    if valor > 0:
        return 1
    elif valor == 0:
        return 0
    elif valor < 0:
        return -1


print(checa_valor(int(input("digite o valor a ser checado (1 = +, -1 = - e 0 = 0): "))))
"""

#  5)
"""


def calc_vol(r):
    return 4/3 * math.pi * r


print(calc_vol(int(input("Digite o valor do raio: "))))

"""

#  6)

"""
def converte_segundos(horas, minutos, segundos):
    print(horas*60*60)
    print(minutos*60)
    print(segundos)


horas = int(input("digite as horas: "))
minutos = int(input("digite os minutos: "))
segundos = int(input("digite os segundos: "))

converte_segundos(horas, minutos, segundos)
"""
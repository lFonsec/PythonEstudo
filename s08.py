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

#   7)
"""


def farenheit(celsius):
    return celsius * (9.0/5.0) + 32.0


print(farenheit(float(input("digite a temperatura: "))))

"""

#   8)

"""
def hipotenusa(cata, catb):
    return math.sqrt(pow(cata, 2) + pow(catb, 2))


cata = int(input("digite o cateto a:"))
catb = int(input("digite o cateto b:"))
print(hipotenusa(cata, catb))
"""

#   9)

"""
def qual_maior(a, b):
    if a > b:
        return f"o valor a({a}) é maior"
    elif a < b:
        return f"o valor b({b}) é maior"
    else:
        return "Sao do mesmo tamanho"


numa = int(input("digite o valor a:"))
numb = int(input("digite o valor b:"))
print(qual_maior(numa, numb))
"""

#  10)


def notas(a, b, c, metodo):
    if metodo == "A" or "a":
        return (a+b+c)/3
    elif metodo == "P" or "p":
        return ((a*5) + (b*3) + (c*2))/10
    else:
        return "Metodo errado"


nota1 = int(input("digite a nota 1: "))
nota2 = int(input("digite a nota 2: "))
nota3 = int(input("digite a nota 3: "))
met = input("digite o metodo A = aritimetica e P = ponderada: ")
print(notas(nota1, nota2, nota3, met))

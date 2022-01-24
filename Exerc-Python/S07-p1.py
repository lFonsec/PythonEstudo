import random
# 1)
"""
A = [1, 0, 5, -2, -5, 7]
print(A[0] + A[1] + A[5])
A[4] = 100
print(A[::])
"""
# 2)
"""
lista = []

for x in range(6):
    lista.append(int(input("Digite um valor inteiro: ")))
print(lista[::])
"""

# 3)
"""
lista = []
lista_quadrada = []

for x in range(10):
    lista.append(int(x))
    aux = lista[x] * lista[x]
    lista_quadrada.append(aux)
print(lista[::])
print(lista_quadrada[::])
"""

# 4)
"""
lista = list(range(8))
x = int(input("Digite um valor X "))
y = int(input("Digite um valor y "))

print(lista[x] + lista[y])
"""
# 5)
"""
lista = list(range(10))
aux = 0
for x in range(10):
    if lista[x] % 2 == 0:
        aux += 1
print(aux)
"""
# 7,8,9)
"""
lista = []
while len(lista) < 10:
    checa = int(input("Digite um valor par: "))
    if checa % 2 != 0:
        print("Valor digitado não é par")
    else:
        lista.append(checa)
print(lista[::-1])
"""
# 9, 10)
"""
lista = []
medGeral = 0
for x in range(15):
    nota = int(input("Digita a nota: "))
    lista.append(nota)
    medGeral += lista[x]
print(medGeral/len(lista))
"""
# 11)
"""

lista = []
soma = 0
negat = 0
for _ in range(10):
    lista.append(random.randint(-10, 10))
for x in lista:
    if x >= 1:
        soma += x
    else:
        negat += 1
print(lista[::])
print(soma, negat)
"""
# 12,13)
"""
lista = []
maior = 0
menor = 100000
soma = 0
for x in range(5):
    digito = int(input("Digite o valor: "))
    if digito > maior:
        maior = digito
    elif digito < menor:
        menor = digito
    lista.append(digito)
    soma += digito
print(lista[::], maior, menor, soma)

aux = 0
for i in range(len(lista)):
    if lista[i] < lista[aux]:
        aux = i
print(aux)
"""
# 38, 36)
"""
lista = []

for x in range(10):
    dig = int(input("Digite o valor: "))
    lista.append(dig)
    lista.sort()
    print(lista[::])
"""
# 37)
"""lista = []
lista2 = []

for x in range(5):
    dig = int(input("Digite o valor: "))
    lista.append(dig)
    lista.sort(reverse=True)
    dig = int(input("Digite o valor para a segunda lista: "))
    lista2.append(dig)
    lista2.sort()
listafinal = lista + lista2
print(listafinal)"""


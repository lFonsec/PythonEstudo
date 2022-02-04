# dictionary comprehension
"""
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numero = [1, 2, 3, 4, 5]
quadrado = {valor: valor ** 2 for valor in numero}
print(quadrado)

chaves = 'abcde'
numero = [1, 2, 3, 4, 5]
mistura = {chaves[i]: numero[i] ** 2 for i in range(0, len(chaves))}

print(mistura)

"""

numero = [1, 2, 3, 4, 5]
resposta = {num: ('par' if num % 2 == 0 else 'impar') for num in numero}
print(resposta)

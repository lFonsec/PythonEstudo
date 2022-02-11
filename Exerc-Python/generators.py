"""

nas aulas anteriores
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension....porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome [0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


# getsizeof() -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# mostra quantos bytes a string está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('ashdfiuhasd'))

print(getsizeof(90))

print(getsizeof(910))

print(getsizeof(92345668823))

print(getsizeof(True))

print(getsizeof(int))

print(getsizeof(str))

print(getsizeof(float))

# Gerando uma lista  com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista  com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista  com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista  com Generator
gen = getsizeof(x * 10 for x in range(1000))

print("-------")
print("list ", list_comp)
print("set ", set_comp)
print("dict ", dic_comp)
print("generator ", gen)

"""

# da para iterar no generator

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)



"""
all() -> retorna true se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel esta vazio

print(all([0, 1, 2, 3])) # false por causa do 0
print(all([7, 1, 2, 3])) # true pq n tem mais o 0
print(all([])) # true pq esta vazio

nomes = ['Carlos', 'Camila', 'Carla', 'Carol', 'Candido', 'Daniel']

print(all([nome[0] == 'C' for nome in nomes])) # false por causa do "Daniel"


print(all([letra for letra in 'ei' if letra in 'aeiou'])) # retorna true pq o ei esta em aeiou
print(all([letra for letra in 'f' if letra in 'aeiou']))  # true pq retorna vazio o que é True por causa do all()

any() -> retorna true se qualquer elemento do iteravel for true se o iteravel for vazio retorna false

print(any([0, 1, 2, 3])) # true por causa dos outros numero tirando o 0
print(any([7, 1, 2, 3])) # true
print(any([])) # false pq esta vazio
"""

nomes = ['Carlos', 'Camila', 'Carla', 'Carol', 'Candido', 'Daniel']

print(any([nome[0] == 'C' for nome in nomes])) # true por causa do any()

print(any([letra for letra in 'ei' if letra in 'aeiou'])) # retorna true pq o ei esta em aeiou
print(any([letra for letra in 'f' if letra in 'aeiou']))  # false pq retorna vazio

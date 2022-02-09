"""

"""
import statistics

dados = [1.3, 1.2, 0.2, -0.1, 4.3, 2.0, 1.9]

media = statistics.mean(dados)
print(media)

# assim como map, filter recebe dois parametros, o primeiro sendo uma funçao e o segundo um iteravel

res = filter(lambda x: x > media, dados)
print(res)
print(list(res))

# assim como a função map() o filter() depois da primeira utilizaçAo dele resultado ele zera


paises = ['', 'Argentina', 'Brasil', 'EUA', '', '', 'Portugal', 'Espanha', '', 'Alemanha']
print(paises)

resp = filter(None, paises)
print(list(resp))

#com lambda

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

print(list(filter(lambda pais: pais != '', paises)))


# a diferença entre map e filter é:
# map: recebe dois parametros, uma funçao e um iteravel e retorna um objeto mapeando a funçao para cada valor do iteravel
# filter: recebe dois parametros, uma funcao e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a funcao


usuarios = [
    {'username': 'samuel', 'tweets': ['Gosto de Metallica', 'Gosto de Black Sabbath']},
    {'username': 'pedro', 'tweets': ['Gosto de Iron Maiden']},
    {'username': 'carla', 'tweets': []},
    {'username': 'pamela', 'tweets': ['Gosto de ACDC']},
    {'username': 'daniel', 'tweets': []},
    {'username': 'igor', 'tweets': ['Gosto de Audioslave']},
    {'username': 'ingride', 'tweets': ['Gosto de Pearl Jam', 'Gosto de Bon Jovi']},

]
print(usuarios)
# filtrar os usuarios que não twittaram nada
print("Inativos")
print(list(filter(lambda u: len(u['tweets']) == 0, usuarios)))
print("Ativos")
print(list(filter(lambda u: u['tweets'] != '', usuarios)))
print("Inativos")
print(list(filter(lambda u: not u['tweets'], usuarios)))
print("Ativos")
print(list(filter(lambda u: u['tweets'], usuarios)))


nomes = ['Vanessa', 'Ana', 'Paula']

# criar uma lista contendo 'sua instrutora é' + nome tendo menos de 5 letras

lista = list(map(lambda nome: f"sua instrutora é {nome}", filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
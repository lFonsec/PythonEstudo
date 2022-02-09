import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))
# forma comum
raios = [2, 5, 7, 8, 9, 10, 1, 3, 4]
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# map é uma função que recebe dois parametros, o primeiro uma função e o segundo um iteravel e retornar um map object
areas = map(area, raios)
print(areas)
print(list(areas))

# map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# apos utilizar a função map() depois da primeira utilizaçAo do resultado ele zera
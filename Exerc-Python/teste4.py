lista = []

for a in range(8):
    b = int(input('Digite o valor: '))
    lista.append(b)

x = int(input('Digite a posição do primeiro numero: '))
y = int(input('Digite o posição do segundo numero: '))

aux = lista[x] + lista[y]

print(aux)

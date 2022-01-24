ePar = 0
soma = 0
ant, atual = 0, 1
aux = 0
limite = 2000_000_0
teste = 0
while soma < limite:
    #print(f'{teste}', end="\n")
    teste = ant + atual
    ant = atual
    atual = teste
    if teste % 2 == 0:
        ePar = teste
        soma = soma + ePar
        print(f'Numero {ePar} é par, e o resultado da soma por enqunato é: {soma}')
    aux += 1
print(soma)

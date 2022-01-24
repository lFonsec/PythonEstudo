resposta = 1
quantosNumeros = int(input('Quantos numeros?: '))
lista = []
numero = 0
aux = 0
maiorNumero = 0
menorNumero = 100000000
auxPar = 0

for quantosNumeros in range(quantosNumeros):
    numero = int(input('digite o numero: '))
    if menorNumero > numero:
        menorNumero = numero
    elif maiorNumero < numero:
        maiorNumero = numero
    lista.append(numero)


while resposta != 0:
    resposta = int(input('Digite o que a opção que vc quer:\n '
                         '1) soma\n '
                         '2) Quantos numeros foram digitados\n '
                         '3) media\n '
                         '4) maior dos numeros\n '
                         '5) menor dos numeros\n '
                         '6) media dos pares\n '
                         '0) Sair\n '))
    if resposta == 1:
        aux = 0
        for quantosNumeros in lista:
            aux = aux + lista[quantosNumeros-1]
        print(f' o numero somado é {aux} \n')
    elif resposta == 2:
        print(f'O numero de digitos é: {quantosNumeros} \n')
    elif resposta == 3:
        aux = 0
        for quantosNumeros in lista:
            aux = aux + lista[quantosNumeros-1]
            aux = aux/quantosNumeros
        print(f'A média é: {aux}')
    elif resposta == 4:
        print(f'O maior numero digitado é: {maiorNumero} \n')
    elif resposta == 5:
        print(f'O menor numero digitado é: {menorNumero} \n')
    elif resposta == 6:
        aux = 0
        for quantosNumeros in lista:
            if lista[quantosNumeros-1] % 2 ==0:
                aux = aux + lista[quantosNumeros-1]
                auxPar = auxPar+1
        aux = aux/auxPar
        print(f'A media dos pares é: {aux} \n')
    elif resposta == 0:
        break







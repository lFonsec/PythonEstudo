"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser string')
    print(f'o texto ({texto}) sera impresso na cor ({cor})')


colore('Pedra', 'vermelho')
#colore(5, 'vermelho')
colore('Pedra', 6)


"""


def colore(texto, cor):
    cores = ('verde', 'vermelho', 'preto', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser string')
    if cor not in cores:
        raise ValueError(f'A cor não é uma cor valida precisa ser {cores}')
    print(f'o texto ({texto}) sera impresso na cor ({cor})')


colore('Pedra', 'vermelho')
colore('Pedra', 'amarelo')


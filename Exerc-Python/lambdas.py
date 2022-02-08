"""
lambda x: 3 * x + 1
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

"""

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


print(nome_completo(' fasdfasd', 'VRESDGESD'))
print(nome_completo('  NCNBC       ', ' 1959 '))

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

autores = ['James Hetfield', 'Ozzy Osborune', 'Rob Halford', 'Tony Iommi', 'Bruce Dickinson', 'Steve Harris',
           'Jimi Hendrix', 'Joe Satriani', 'Steve Vai', 'corey Taylor']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print("Odernando pelo sobrenome: ", autores)

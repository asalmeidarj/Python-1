""" Triângulo com maior b + c """


def triangulo():
    print('Entre com 3 valores, o maior primeiro: ')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    if a < b+c:
        print('Forma triângulo')
    else:
        print('Não forma triângulo')


triangulo()

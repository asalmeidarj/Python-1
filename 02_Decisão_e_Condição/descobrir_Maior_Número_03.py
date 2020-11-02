""" Imprimir na tela número maior """


def maiorNumero():
    a = int(input('a= '))
    b = int(input('b= '))
    c = int(input('c= '))
    print('o maior número é: ')
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else:
            print(c)


maiorNumero()

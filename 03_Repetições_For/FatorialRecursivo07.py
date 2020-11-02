""" Fatorial Recursivo """


def fatorial(numero):
    if numero <= 1:
        return 1
    return numero * fatorial(numero - 1)  # chamada recursivo


for i in range(11):
    print(f'{i} != {fatorial(i)}')

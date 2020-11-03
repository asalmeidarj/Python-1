""" exemplos de listas """


def listas():
    lista_01 = [1, 99, 2, 88, 3, 77, 10, 20, 70, 50]
    lista_02 = ['a', 'b', 'z', 'x', 'c', 'd', 'e', 'f', 'y', 'j']
    lista_03 = []
    lista_04 = list(range(11))  # executa o range de 1 até 10
    lista_05 = list('clD leinaD')

    lista_01.sort()  # exemplo para ordenar a lista numérica
    print(lista_01)

    lista_02.sort(reverse=True)  # exemplo para ordenar inversa
    print(lista_02)

    lista_03.append(100)  # append adiciona um elemento na lista
    print(lista_03)

    print(len(lista_04))  # len faz a leitura de elementos da lista

    lista_05.reverse()  # inverte sequência da lista
    print(lista_05)


listas()

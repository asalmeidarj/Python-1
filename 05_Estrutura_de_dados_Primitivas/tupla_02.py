""" Exemplos de Tupla """


def tupla():
    tupla_01 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tupla_02 = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    tupla_03 = tupla_01 + tupla_02  # junta as duas tuplas
    tupla_04 = ('a', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd', 'e')

    print(tupla_01)
    print(tupla_02)
    print(tupla_03)  # tuplas são imutáveis
    print(tupla_04.count('d'))  # conta quantas letras d possuo na tupla


tupla()

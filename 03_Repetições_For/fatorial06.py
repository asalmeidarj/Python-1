""" Fatorial """

def fatorial():
    n = int(input('Digite o número e direi o fatorial: '))
    fatorial = 1
    for i in range(2, n+1):
        fatorial *= i
    print(fatorial)


fatorial()
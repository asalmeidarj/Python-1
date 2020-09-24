"""
Mostre o somatório S (a, b) de de uma sequência S qualquer tal que S (a, b) é o
somatório dos elementos da posição a até b de uma sequência S.
"""

S = [numero for numero in range(100) if numero % 2 != 0]  # Uma sequência de números Ímpares

inf = int(input('Limite inferior: '))
sup = int(input('Limite superior: '))

print(S[inf-1:sup])
print(f'A soma dos elementos das posições de  {inf} a {sup} é {sum(S[inf-1:sup])}')

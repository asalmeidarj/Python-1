"""
Implemente um programa que receba o valor de uma mercadoria, o número de meses para pagar, e
a taxa de juros mensal. 
Imprima o valor das parcelas, considerando juros cumulativos.
"""

#!/usr/bin/python

from math import pow  # essa linha pode ser comentada de acordo com a versão do Python (pep 570)

"""Recebe o valor da mercadoria, o número de parcelas e a taxa de juros."""
"""Retorna o valor das parcelas fixas."""
def parcela(valor, periodo, taxa): 
    valor = float(valor)
    periodo = float(periodo)
    taxa = float(taxa)
    parcela = valor*taxa/(1-pow((1+taxa), -periodo))
    return f'{parcela:.2f}'


valor = input('Valor da mercadoria: ')
periodo = input('Número de parcelas: ')
taxa = input('Taxa de juros (Ex.: 0.02 = 2%): ')
print(f'Pagamento em {int(periodo)}x de R$ {parcela(valor, periodo, taxa)}')

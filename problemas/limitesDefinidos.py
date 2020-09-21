"""
Implemente um programa para imprimit a função f(x) = sin(x² + exp(x))
entre dois limites definidos pelo usuário
"""
# programa em execução dentro de uma virtualenv

import numpy as np                # pip install numpy
import matplotlib.pyplot as plt   #pip install matplotlib

print('Determine o limite inferior e superior do gráfico f(x)')
print('f(x) = sin(x^2 + exp(x)) \n')
inf = float(input('Inf: '))
sup = float(input('Sup: '))
dominio = np.linspace(inf, sup, 1000)
imagem = list(map(lambda x: np.sin(pow(x, 2) + np.exp(x)), dominio))

plt.title('Gerar o gráfico da função f(x) = sin(x^2 + exp(x)) no intervalo dado')
plt.plot(dominio, imagem)
plt.show()

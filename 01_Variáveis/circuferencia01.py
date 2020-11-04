"""  esfera utilizando apenas input  """

def comprimento():
    r = float(input('Entre com o raio: '))
    print('Circunferência: ', 2*3.14159*r)
    print('Área do círculo: ', 3.14159*r**2)
    print('Área da esfera: ', 4*3.14159*r**2)


comprimento()

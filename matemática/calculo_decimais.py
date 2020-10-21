""" Realizar cálculos decimais precisos """

from decimal import Decimal  

def decimal():  
    x = Decimal('4.2')
    y = Decimal('2.1')
    z = x + y  # calcular 4.2 + 2.1
    print(z == Decimal('6.3'))  # comparação entre números
    print() 
    print(z)  


decimal()  # chamando a função 

""" Fazer calculos com frações """

from fractions import Fraction


def fracoes():
    a = Fraction(5,4)
    b = Fraction(7,16)
    c = a*b
    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    
    print(a+b) 
    print(a*b) 
    print(c.numerator)  
    print(c.denominator)
    print(float(c))  # convertendo para número flutuante
    print(c.limit_denominator(8))  # limitar denominador de um valor
    print(y)  # converte um número de ponto flutuante para uma fração


fracoes()
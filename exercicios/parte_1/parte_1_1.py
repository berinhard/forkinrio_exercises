#-*- coding: utf-8 -*-

'''
Implementar duas funções:
  * Uma que converta temperatura em graus Celsius para Fahrenheit.
  * Outra que converta temperatura em graus Fahrenheit para Celsius.

#F = (9/5)*C + 32
#C = (F - 32)*(5/9)
'''

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5.0 / 9)

def celsius_to_fahrenheit(celsius):
    return (9.0/5) * celsius + 32

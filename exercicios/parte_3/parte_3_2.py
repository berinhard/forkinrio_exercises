#-*- coding: utf-8 -*-
'''
2. Implementar o gerador de numeros primos como uma expressao (dica: use
o modulo itertools).
'''

import itertools as it

def primo(num):
    for x in range(3, num / 2, 2):
        if not(num % x):
            return False
    else:
        return True

count = 0
if __name__ == '__main__':
    f = open('primos2.txt', 'w')
    #tem como fazer a função primo usando o lambda?
    for num in it.ifilter(primo, it.ifilter(lambda num: num % 2 or num == 2, it.count(2))):
        f.write(str(num) + '\n')

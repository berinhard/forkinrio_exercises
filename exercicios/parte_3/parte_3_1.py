#-*- coding: utf-8 -*-
'''
1. Implementar um gerador de números primos.
'''

def gera_primos():

    num = 1
    while True:        
        num += 1

        #o numero 2 já é primo
        if num == 2:
            yield num

        #não dá o yield nos pares
        if not(num % 2):
            continue
        
        #caso ele passe por todos os números retornados no range, ele é primo
        #caso contrário é só dar o break no for para ele avaliar o próxim
        for i in range (3, num / 2, 2):
            if not(num % i):
                break
        else:
            yield num

if __name__ == '__main__':
    f = open('primos1.txt', 'w')
    for num in gera_primos():
        f.write(str(num) + '\n')

#-*- coding: utf-8 -*-
'''
3. Implementar um gerador que produza tuplas com as cores do padrao RGB
(R, G e B variam de 0 a 255) usando xrange() e uma funcao que produza uma
lista com as tuplas RGB usando range(). Compare a performance.
'''
import time

def gera_rgb_range():
    r, g, b = 0, 0, 0
    for i in range(256):
        r = i
        for j in range(256):
            g = j
            for k in range(256):
                b = k
                yield (r, g, b)

def gera_rgb_xrange():
    r, g, b = 0, 0, 0
    for i in xrange(256):
        r = i
        for j in xrange(256):
            g = j
            for k in xrange(256):
                b = k
                yield (r, g, b)

if __name__ == '__main__':
    
    for i in range(1, 6):

        print '\nAmostra %d: \nUsando range():' %i
        inicio = time.time()
        for i in gera_rgb_range():
            pass
        fim = time.time()
        print '%f segundos' %(fim - inicio)

        print 'Usando xrange():'
        inicio = time.time()
        for i in gera_rgb_xrange():
            pass
        fim = time.time()
        print '%f segundos' %(fim - inicio)

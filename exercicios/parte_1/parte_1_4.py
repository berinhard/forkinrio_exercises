#-*- coding: utf-8 -*-

'''
4. Implementar uma função que receba uma lista e retorne a soma, a
média e a variação dos valores.
'''

def mega_function(lista_de_valores):
    numero_de_elementos = len(lista_de_valores)
    soma = sum(lista_de_valores)
    media = float(soma) / numero_de_elementos
    variacao = max(lista_de_valores) - min(lista_de_valores)
    return soma, media, variacao

if __name__ == '__main__':
    lista_input = [1, 2, 3, 4, 5, 6]
    tupla_de_retorno = mega_function(lista_input)
    print lista_input
    print 'Soma: %d' %tupla_de_retorno[0]
    print 'Media: %d' %tupla_de_retorno[1]
    print 'Variacao: %d' %tupla_de_retorno[2]


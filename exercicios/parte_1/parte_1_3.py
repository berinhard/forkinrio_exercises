#-*- coding: utf-8 -*-

'''
Implementar uma função que receba uma lista de listas de comprimentos
quaisquer e retorne uma lista de uma dimensão.
'''

#lista contendo N tuplas com Y comprimentos
#o retorno deve ser o multiplicatórios desses comprimentos

#função
def gera_dimensoes(lista_comprimentos):
    
    lista_dimensoes = []

    for tupla in lista_comprimentos:
        dimensao = 1
        for comprimento in tupla:
            dimensao = dimensao * comprimento
        lista_dimensoes.append(dimensao)

    return lista_dimensoes

#execução
lista = [(1, 2, 3),
         (4, 2),
         (6, 7, 9, 7),
         (9, 9)]
print gera_dimensoes(lista)

#-*- coding: utf-8 -*-

'''
Escreva uma função que:
   * Receba uma frase como parâmetro.
   * Retorne uma nova frase com cada palavra com as letras invertidas.
'''

#função
def inverte_todas_palavras_da_frase(frase):
    lista_palavras = frase.split()

    # com list comprehension
    #lista_palavras_invertidas = [palavra[::-1] + ' ' for palavra in lista_palavras]
    #return ''.join(lista_palavras_invertidas)

    # sem list comprehension
    frase_invertida = ''
    for palavra in lista_palavras:
        frase_invertida = frase_invertida + palavra[::-1] + " "
    return frase_invertida[0:-1]

#codigo executável
minha_frase = raw_input('Escreva sua frase: ')
minha_frase_invertida = inverte_todas_palavras_da_frase(minha_frase)
print minha_frase_invertida



#-*- coding: utf-8 -*-

'''
6. Crie uma função que:
    ▪ Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão
       igual) e um booleano (reverso, falso por padrão).
    ▪ Retorne dados ordenados pelo item indicado pela chave e em ordem
       decrescente se reverso for verdadeiro.
'''

def minha_sorte(lista, index = 0, reverso = False):

    #pedir explicação usando cmp
    def minha_funcao_chave(tupla):
        return tupla[index]

    return sorted(lista, key = minha_funcao_chave, reverse = reverso)

if __name__ == '__main__':
    a = [(3, 1, 2), (3, 2, 7), (1, 9 , 4, 5)]
    print minha_sorte(a, 2)

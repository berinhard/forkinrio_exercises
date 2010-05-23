#coding:utf-8

'''
2. Crie uma classe derivada de lista com um método retorne os elementos da
lista sem repetição.
'''

import unittest

class MinhaLista(list):

    def lista_sem_repeticao(self):
        lista_retorno = []

        for elemento in self:
            if not elemento in lista_retorno:
                lista_retorno.append(elemento)

        return lista_retorno

class TestMinhaLista(unittest.TestCase):

    def test_lista_vazia_retorna_lista_vazia(self):
        lista = MinhaLista([])
        self.assertEquals([], lista.lista_sem_repeticao())

    def test_lista_somente_com_um_elem_retorna_a_propria_lista(self):
        entrada = [1]
        lista = MinhaLista(entrada)
        self.assertEquals(entrada, lista.lista_sem_repeticao())

    def test_lista_com_repeticao_retorna_a_propria_lista_sem_repeticao(self):
        entrada = [1, 'abc', 2, 3, 3, 'abc']
        lista = MinhaLista(entrada)
        self.assertEquals([1, 'abc', 2, 3], lista.lista_sem_repeticao())

    def test_lista_sem_repeticoes_retorna_a_propria_lista(self):
        entrada = [1, 'abc', 2, 3]
        lista = MinhaLista(entrada)
        self.assertEquals(entrada, lista.lista_sem_repeticao())

if __name__ == '__main__':
    unittest.main()

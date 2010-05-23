#coding:utf-8
'''
1. Crie uma classe que modele um quadrado, com um atributo lado e os
métodos: mudar valor do lado, retornar valor do lado e calcular área.
'''

import unittest

class Quadrado(object):

    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, novo_lado):
        self.lado = novo_lado

    @property
    def area(self):
        return self.lado ** 2

class TestQuadrado(unittest.TestCase):

    def setUp(self):
        self.quadrado = Quadrado(4)

    def test_set_lado_5_get_lado_5(self):
        self.quadrado.set_lado(5)
        self.assertEquals(5, self.quadrado.get_lado())

    def test_area_quadrado_lado_4_resulta_16(self):
        self.assertEquals(16, self.quadrado.area)

if __name__ == '__main__':
    unittest.main()

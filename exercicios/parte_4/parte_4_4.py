#coding: utf-8

'''
4. Implementar uma classe Vetor:
    ▪ Com coordenadas x, y e z.
    ▪ Que suporte soma, subtração, produto escalar e produto vetorial.
    ▪ Que calcule o módulo (valor absoluto) do vetor.
'''

from math import sqrt
import unittest

class Vetor(object):

    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __add__(self, outro_vetor):
        return Vetor(self.x + outro_vetor.x, self.y + outro_vetor.y, self.z + outro_vetor.z)

    def __sub__(self, outro_vetor):
        return Vetor(self.x - outro_vetor.x, self.y - outro_vetor.y, self.z - outro_vetor.z)

    def __mul__(self, valor):
        if type(valor) == self.__class__:
            novo_vetor = Vetor(self.x * valor.x, self.y * valor.y, self.z * valor.z)
            return novo_vetor.x + novo_vetor.y + novo_vetor.z
        if type(valor) == int:
            return Vetor(self.x * valor, self.y * valor, self.z * valor)

    def __eq__(self, outro_vetor):
        return self.x == outro_vetor.x and self.y == outro_vetor.y and self.z == outro_vetor.z

    def __repr__(self):
        return '(%d, %d, %d)' % (self.x, self.y, self.z)

    def produto_vetorial(self, outro_vetor):
        '''http://pt.wikipedia.org/wiki/Produto_vetorial
        {i}(a2*b3) + {}j}(a3*b1) + {k}(a1*b2) - {i}(a3*b2) - {j}(a1*b3) - {k}(a2*b1)
        '''
        x = self.y * outro_vetor.z - self.z * outro_vetor.y
        y = self.z * outro_vetor.x - self.x * outro_vetor.z
        z = self.x * outro_vetor.y - self.y * outro_vetor.x
        return Vetor(x, y, z)

    @property
    def modulo(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

class TestVetor(unittest.TestCase):

    def setUp(self):
        self.vetor1 = Vetor(1, 2, 3)
        self.vetor2 = Vetor(4, 5, 6)

    def test_soma_vetor1_com_vetor2_resultado_5_7_9(self):
        vetor_resultante = Vetor(5, 7, 9)
        self.assertEquals(vetor_resultante, self.vetor1 + self.vetor2)

    def test_subtracao_vetor2_por_vetor1_resultado_3_3_3(self):
        vetor_resultante = Vetor(3, 3, 3)
        self.assertEquals(vetor_resultante, self.vetor2 - self.vetor1)

    def test_produto_escalar_vetor2_por_5_resultando_20_25_30(self):
        vetor_resultante = Vetor(20, 25, 30)
        self.assertEquals(vetor_resultante, self.vetor2 * 5)

    def test_produto_escalar_vetor2_pelo_vetor_1_resultando_32(self):
        self.assertEquals(32, self.vetor2 * self.vetor1)

    def test_modulo_vetor1_resultando_sqrt_de_14(self):
        self.assertEquals(sqrt(14), self.vetor1.modulo)

    def test_produto_vetorial_vetor1_por_vetor2_resultando_minus3_6_minus3(self):
        vetor_resultante = Vetor(-3, 6, -3)
        self.assertEquals(vetor_resultante, self.vetor1.produto_vetorial(self.vetor2))

if __name__ == '__main__':
    unittest.main()

#coding: utf-8

'''
5. Implemente um módulo com:
    ▪ Uma classe Ponto, com coordenadas x, y e z.
    ▪ Uma classe Linha, com dois pontos A e B, e que calcule o comprimento
      da linha.
    ▪ Uma classe Triangulo, com dois pontos A, B e C, que calcule o
      comprimento dos lados e a área.
'''

import unittest
from math import fabs, sqrt
from parte_4_4 import Vetor

class Ponto(object):
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def dist_outro_ponto(self, ponto):
        '''
        É o conceito de módulo! Bazinga!
        '''
        vetor1 = Vetor(self.x, self.y, self.z)
        vetor2 = Vetor(ponto.x, ponto.y, ponto.z)
        vetor_modulo = vetor2 - vetor1
        return vetor_modulo.modulo

class Linha(object):
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1

    @property
    def comprimento(self):
        return self.p1.dist_outro_ponto(self.p0)

class Triangulo(object):
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    @property
    def comprimento_p0_p1(self):
        return self.p0.dist_outro_ponto(self.p1)

    @property
    def comprimento_p0_p2(self):
        return self.p0.dist_outro_ponto(self.p2)

    @property
    def comprimento_p1_p2(self):
        return self.p1.dist_outro_ponto(self.p2)

    @property
    def area(self):
        '''
        Essa eu não sei mesmo como fazer a projeção do ponto em 90º com a base
        para ter a altura usada no cálculo da área...
        '''
        pass

class TestLinha(unittest.TestCase):

    def setUp(self):
        ponto_inicial = Ponto ()
        ponto_final = Ponto (x=3)
        self.linha = Linha(ponto_inicial, ponto_final)

    def test_calcula_o_comprimento_com_pontos_somento_no_eixo_x_resultanto_em_3(self):
        ponto_inicial = Ponto(x=6)
        ponto_final = Ponto(x=3)
        linha = Linha(ponto_inicial, ponto_final)
        self.assertEquals(fabs(3), linha.comprimento)

    def test_calcula_o_comprimento_com_pontos_somento_no_eixo_y_resultanto_em_3(self):
        ponto_inicial = Ponto(y=6)
        ponto_final = Ponto(y=3)
        linha = Linha(ponto_inicial, ponto_final)
        self.assertEquals(fabs(3), linha.comprimento)

    def test_calcula_o_comprimento_com_pontos_somento_no_eixo_z_resultanto_em_3(self):
        ponto_inicial = Ponto(z=6)
        ponto_final = Ponto(z=3)
        linha = Linha(ponto_inicial, ponto_final)
        self.assertEquals(fabs(3), linha.comprimento)

    def test_calcula_o_comprimento_com_pontos_no_eixo_x_e_y_resultanto_em_5(self):
        ponto_inicial = Ponto(x=0, y=0)
        ponto_final = Ponto(x=3, y=4)
        linha = Linha(ponto_inicial, ponto_final)
        self.assertEquals(5, linha.comprimento)

    def test_calcula_comprimento_com_pontos_no_eixo_x_y_z_resultando_em_sqrt132(self):
        ponto_inicial = Ponto(x=1, y=12, z=7)
        ponto_final = Ponto(x=3, y=4, z=-1)
        linha = Linha(ponto_inicial, ponto_final)
        self.assertEquals(sqrt(132), linha.comprimento)

    def test_calcula_comprimento_triangulo(self):
        p0 = Ponto(x=0, y=2, z=3)
        p1 = Ponto(x=2, y=7, z=0)
        p2 = Ponto(x=5, y=4, z=-2)
        triangulo = Triangulo(p0, p1, p2)
        self.assertEquals(sqrt(38), triangulo.comprimento_p0_p1)
        self.assertEquals(sqrt(22), triangulo.comprimento_p1_p2)
        self.assertEquals(sqrt(54), triangulo.comprimento_p0_p2)

if __name__ == '__main__':
    unittest.main()

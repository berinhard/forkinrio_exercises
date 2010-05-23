#coding:utf-8

'''
3. Implemente uma classe Carro com as seguintes propriedades:
    ▪ Um veículo tem um certo consumo de combustível (medidos em km /
      litro) e uma certa quantidade de combustível no tanque.
    ▪ O consumo é especificado no construtor e o nível de combustível inicial
      é 0.
    ▪ Forneça um método mover(km) que receba a distância em quilômetros e
      reduza o nível de combustível no tanque de gasolina.
    ▪ Forneça um método gasolina(), que retorna o nível atual de
      combustível.
    ▪ Forneça um método abastecer(litros), para abastecer o tanque.
'''

import unittest

class Carro(object):

    def __init__(self, consumo, combustivel=0):
        self.consumo = consumo
        self.combustivel = combustivel

    def abastecer(self, litros):
        self.combustivel += litros

    def gasolina(self):
        return self.combustivel

    def mover(self, km):
        if not self.combustivel:
            print 'Tanque vazio!'
            pass
        gasto = km / self.consumo
        if gasto > self.combustivel:
            print 'Combustivel insuficiente!'
            km = self.combustivel * self.consumo
            gasto = self.combustivel
        self.combustivel -= gasto
        return km

class TestCarro(unittest.TestCase):

    def setUp(self):
        self.carro = Carro(16.0, 20.0)

    def test_anda_16_km_com_sucesso_e_19_litros_sobram(self):
        km = 16
        self.assertEquals(km, self.carro.mover(km))
        self.assertEquals(19, self.carro.gasolina())

    def test_anda_320_km_e_zera_o_tanque(self):
        km = 320
        self.assertEquals(km, self.carro.mover(km))
        self.assertEquals(0, self.carro.gasolina())

    def test_tenta_andar_340_km_anda_somente_320_e_zera_o_tanque(self):
        km = 340
        self.assertEquals(320, self.carro.mover(km))
        self.assertEquals(0, self.carro.gasolina())

    def test_tenta_andar_10km_com_o_tanque_vazio_e_nao_anda_nada(self):
        km = 10
        self.carro.combustivel = 0
        self.assertEquals(0, self.carro.mover(km))
        self.assertEquals(0, self.carro.gasolina())

    def test_tenta_andar_10km_com_o_tanque_vazio_e_nao_anda_nada_abastece_e_anda(self):
        km = 16
        self.carro.combustivel = 0
        self.assertEquals(0, self.carro.mover(km))
        self.assertEquals(0, self.carro.gasolina())
        self.carro.abastecer(20)
        self.assertEquals(km, self.carro.mover(km))
        self.assertEquals(19, self.carro.gasolina())

if __name__ == '__main__':
    unittest.main()

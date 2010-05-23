#-*- coding: utf-8 -*-

import unittest
from parte_1_2 import eh_primo

class TestConversaoEscalas(unittest.TestCase):

    def setUp(self):
        self.numeros = range(100)

    def test_1_nao_eh_primo(self):
        self.assertFalse(eh_primo(self.numeros[0] + 1))

    def test_6_nao_eh_primo(self):
        self.assertFalse(eh_primo(self.numeros[5] + 1))

    def test_2_eh_primo(self):
        self.assertTrue(eh_primo(self.numeros[1] + 1))

    def test_7_eh_primo(self):
        self.assertTrue(eh_primo(self.numeros[6] + 1))

if __name__ == '__main__':
    unittest.main()


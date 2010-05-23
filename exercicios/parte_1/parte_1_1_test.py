#-*- coding: utf-8 -*-

import unittest
from parte_1_1 import fahrenheit_to_celsius
from parte_1_1 import celsius_to_fahrenheit

class TestConversaoEscalas(unittest.TestCase):

    def test_fahrenheit_to_celsius_one(self):
        self.assertEqual(fahrenheit_to_celsius(68), 20)

    def test_fahrenheit_to_celsius_one(self):
        self.assertEqual(fahrenheit_to_celsius(-14), -25.555555555555557)

    def test_fahrenheit_to_celsius_one(self):
        self.assertEqual(fahrenheit_to_celsius(0), -17.77777777777778)

    def test_celsius_to_fahrenheit_one(self):
        self.assertEqual(celsius_to_fahrenheit(30), 86)

    def test_celsius_to_fahrenheit_two(self):
        self.assertEqual(celsius_to_fahrenheit(-15), 5)

    def test_celsius_to_fahrenheit_three(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

if __name__ == '__main__':
    unittest.main()


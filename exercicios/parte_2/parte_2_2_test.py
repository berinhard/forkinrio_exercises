#-*- coding: utf-8 -*-

import unittest
from parte_2_2 import matrix_sum
from parte_2_2 import camel_case

class TestModuloExercicio2(unittest.TestCase):

    def test_mat_1_2_3_4_plus_mat_3_4_5_6_result_mat_4_6_8_10(self):
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[3, 4], [5, 6]]
        self.assertEqual(matrix_sum(matrix_a, matrix_b), [[4, 6], [8, 10]])

    def test_bernardo_botelho_fontes_camel_case_BernardoBotelhoFontes(self):
        name = 'bernardo botelho fontes'
        self.assertEqual(camel_case(name), 'BernardoBotelhoFontes')

if __name__ == '__main__':
    unittest.main()


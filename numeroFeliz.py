#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Comprobar si un número es feliz

import unittest

def numero_feliz(num):
    feliz = False
    for x in range(0, 20):
        lista_num = lista_digitos(num)
        num = suma_cuadrado(*lista_num)
        if num == 1:
            feliz = True
    return feliz

def suma_cuadrado(*nums):
    suma = 0
    for num in nums:
        suma += num**2
    return suma

def lista_digitos(num):
    lista_num = []
    while num > 0:
        lista_num.append(num % 10)
        num = num // 10
    return lista_num
    

class DoblesDeImparesTest(unittest.TestCase):
    def test_devuelve_True_si_es_feliz(self):
        self.assertTrue(numero_feliz(19))

    def test_devuelve_False_si_no_es_feliz(self):
        self.assertFalse(numero_feliz(2))

    def test_devuelve_suma_cuadrados(self):
        self.assertEqual(suma_cuadrado(*[4, 2]), 20)

    def test_separa_digitos_en_lista(self):
        self.assertEqual(lista_digitos(19), [9, 1])

if __name__ == '__main__':
    unittest.main()

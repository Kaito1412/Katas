#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dados dos números enteros positivos a <= b, generar la lista de los 
# dobles de todos los impares x tales que a <= x <= b.
# 
# Vamos, tomar los números impares entre a y b pero multiplicados por 
# dos.

# Por ejemplo, dados 2 y 11, deberá devolver [6, 10, 14, 18, 22].


import unittest

def esImpar(numero):
    return numero % 2 != 0

def anyadirALaListaSiEsImpar(numero, lista):
    if (esImpar(numero)):
        lista.append(numero * 2)

def doblesDeImpares(num1, num2):
    lista = []
    for i in range(num1, (num2 + 1)):
        anyadirALaListaSiEsImpar(i, lista)
    
    return lista

class DoblesDeImparesTest(unittest.TestCase):
    def test_devuelveListaVaciaSiAyBiguales(self):
        self.assertEqual([], doblesDeImpares(2, 2))

    def test_devuelveAlgoSiAyBdistintos(self):
        self.assertEqual(1, len(doblesDeImpares(2, 4)))

    def test_devuelveSeisYDiezAlRecibir2y6(self):
        self.assertEqual([6, 10], doblesDeImpares(2,6))

if __name__ == '__main__':
    unittest.main()

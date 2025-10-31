#!/usr/bin/env python
'''Tasca 08 Bones pràctiques. Recuperar el codi escrit a la pràctica anterior,
Divisió entera, i aplica els principis de bones pràctiques
Programació - 1r Batxillerat - Curs 2023-24
Aquest programa demana que introdueixi dos nombres enters:
un com a dividend i l'altre com a divisor. A continuació, el programa
realitza la divisió entera entre aquests dos nombres i calcula tant
el quocient com el residu de la divisió.
'''
__author__ = "Dong Yi"

__email__= "yzheng@instituticaria.cat"

__date__ = "2025/10/31"

dividend = int(input("A: "))
divisor = int(input("B: "))

quocient = dividend // divisor
residu = dividend % divisor

print("Divisió:", dividend, "/", divisor)
print("Quocient:", quocient)
print("Residu:", residu)


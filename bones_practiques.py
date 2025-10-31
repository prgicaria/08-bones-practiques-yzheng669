#!/usr/bin/env python
'''Tasca 08 Bones pràctiques. Recuperar el codi escrit a la pràctica anterior, Divisió entera
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Aquest programa demana que introdueixi dos nombres enters: un dividend i un divisor.
A continuació, el programa calcula la divisió entera d’aquests dos nombres.Abans de fer la divisió, el programa comprova que el divisor no sigui
zero, ja que dividir entre zero no està permès.
' 
__author__ = "Dong Yi"
__email__ = "yzheng@instituticaria.cat"
__date__ = "2025/10/31"
'''

dividend = int(input("A: "))
divisor = int(input("B: "))

quocient = dividend // divisor
residu = dividend % divisor

print("Divisió:", dividend, "/", divisor)
print("Quocient:", quocient)
print("Residu:", residu)

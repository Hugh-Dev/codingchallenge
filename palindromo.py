#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#▞▀▖     ▌▗        ▞▀▖▌     ▜▜              ▞▀▖▞▀▖▞▀▖▛▀▖▛▀▖
#▌  ▞▀▖▞▀▌▄ ▛▀▖▞▀▌ ▌  ▛▀▖▝▀▖▐▐ ▞▀▖▛▀▖▞▀▌▞▀▖ ▙▄▌▚▄ ▙▄▌▙▄▘▙▄▘
#▌ ▖▌ ▌▌ ▌▐ ▌ ▌▚▄▌ ▌ ▖▌ ▌▞▀▌▐▐ ▛▀ ▌ ▌▚▄▌▛▀  ▌ ▌▖ ▌▌ ▌▌  ▌
#▝▀ ▝▀ ▝▀▘▀▘▘ ▘▗▄▘ ▝▀ ▘ ▘▝▀▘ ▘▘▝▀▘▘ ▘▗▄▘▝▀▘ ▘ ▘▝▀ ▘ ▘▘  ▘ - PyConAr 2020

"""
@author Hugo Ramírez
@copyright Hugo Ramírez
@cto Hughpythoneer
@date 20-11-2020
@version 2.0.0
"""

import os

"""class Palindromo():
    def Verificar(self, cadena):
        self.reversed = ''.join(reversed(cadena))
        if cadena == self.reversed:
            print("Es un palíndromo")
            return True
        else:
            print("No es un palíndromo")
            return False

plm = Palindromo()
cadena_original = input('cadena: ')
resultado = plm.Verificar(cadena_original)
print(resultado)"""


def Verificar(cadena):
    reverso = ''.join(reversed(cadena))
    if cadena == reverso:
        return True
    else:
        return False

def Completar(cadena):
    reverso = ''.join(reversed(cadena))
    coinciden = []
    nocoinciden = []
    original = []
    inverso = []    
    for x in cadena:
        original.append(x)
    for i in reverso:
        inverso.append(i)
    for x in range(0,len(original)):
        if original[x] == inverso[x]:
            coinciden.append(inverso[x])
        elif original[x] != inverso[x]:
            nocoinciden.append(inverso[x])
    
    if len(coinciden) == 0:
        return len(reverso)
    else:
        print(coinciden)
        print(len(original), '-', len(coinciden))
        completa =  len(original) - len(coinciden)
        return completa

if __name__ == '__main__':
    choice = input("Desea leer un archivo y/n: ")
    if choice == "n":
        cadena = input("Cadena de caracteres a evaluar: ")
        response = Verificar(cadena)
        if response == True:
            print('Es palíndromo no necesita ser completado')
        else:
            completado = Completar(cadena)
            print('La cadena necesita {} caracteres'.format(completado))

    elif choice == "y":
        ruta = input("Nombre del archivo: ")
        lista = []
        f = open(str(ruta), "r")
        for linea in f:
            lista.append(linea)
        f.close()
        cadena = str(lista[1].replace('\n', ''))
        response = Verificar(cadena)
        if response == True:
            print('Es palíndromo no necesita ser completado')
        else:
            completado = Completar(cadena)
            print('La cadena necesita {} caracteres para ser un palíndromo'.format(completado))
        
    else:
        print('(-.-) La respuesta ({}) es incorrecta vuelva a intentarlo!'.format(choice))
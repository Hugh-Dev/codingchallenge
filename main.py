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
import sys
import difflib
import cmd
import os
import difflib

class Palindromo():
    def Menu(self, arg):
        if arg <= 10:
            if arg == 1:
                self.lista = []
                f = open("PALIN1.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        #diff_str = list(difflib.ndiff(string, string_reversed))
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = len(diff_str) - len(string)

                        #print(''.join(difflib.restore(diff_str, which=1)))
                        #diff = difflib.Differ()
                        #diff_str = diff.compare(string_lines, string_reversed_lines)
                        #print(''.join(diff_str))


                        print("Para que sea un palíndromo se deben agregar al menos {} caracteres".format(result).replace('-', ''))

            elif arg == 2:
                self.lista = []
                f = open("PALIN2.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    print(len(string_reversed))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str)) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 3:
                self.lista = []
                f = open("PALIN3.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str[1])) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 4:
                self.lista = []
                f = open("PALIN4.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str[1].replace('+ ', ''))) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 5:
                self.lista = []
                f = open("PALIN5.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str)) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 6:
                self.lista = []
                f = open("PALIN6.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str)) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 7:
                self.lista = []
                f = open("PALIN7.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = self.lista[1].replace('\n', '')
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    if str(string) == ''.join(reversed(string)):
                        print("Es un palíndromo")
                    else:
                        string_reversed = ''.join(reversed(string))

                        #diff = difflib.Differ()
                        #diff_str = diff.compare(string, test)
                        #print(''.join(diff_str))

                        #string_lines = string.splitlines()
                        #string_reversed_lines = string_reversed.splitlines()
                        #diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))

                        diff_str = list(difflib.ndiff(string, string_reversed))
                        print(diff_str)

                        result = len(diff_str) - len(string)
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 8:
                self.lista = []
                f = open("PALIN8.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str)) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 9:
                self.lista = []
                f = open("PALIN9.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str)) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

            elif arg == 10:
                self.lista = []
                f = open("PALIN10.IN", "r")
                for linea in f:
                    self.lista.append(linea)
                f.close()
                string = str(self.lista[1].replace('\n', ''))
                verify = input('el archivo posee un string de longitud {} desea continuar y/n :'.format(self.lista[0]))
                if verify == 'y':
                    string_reversed = str(''.join(reversed(string)))
                    if string == string_reversed:
                        print("Es un palíndromo")
                    else:
                        string_lines = string.splitlines()
                        string_reversed_lines = string_reversed.splitlines()
                        diff_str = list(difflib.ndiff(string_lines, string_reversed_lines))
                        result = int(len(diff_str)) - int(self.lista[0])
                        print("Para que sea un palíndromo se deben agregar {} caracteres".format(result).replace('-', ''))

        else:
            msg = 'choice invalid'
            return msg




pl = Palindromo()
print('Seleccione la opcion de archivo en el que desea trabajar:')
print('\n 1) - PALIN1.IN: \n 2) - PALIN2.IN: \n 3) - PALIN3.IN: \n 4) - PALIN4.IN: \n 5) - PALIN5.IN: \n 6) - PALIN6.IN: \n 7) - PALIN7.IN: \n 8) - PALIN8.IN: \n 9) - PALIN9.IN: \n 10) - PALIN10.IN: ')
choice = input('choice: ')
result = pl.Menu(int(choice))
print(result)

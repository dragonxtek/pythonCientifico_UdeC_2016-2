#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2016 Nicolás Boettcher
# This file is part of pythonCientifico_UdeC_2016-2
#
# pythonCientifico_UdeC_2016-2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pythonCientifico_UdeC_2016-2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

from random import randint
import sys

def crealista(inicio,fin,largo=100):
    """
    Crea una lista de un largo específico
    con números entre inicio y fin
    :param inicio: int
    :param fin: int
    :param largo: int
    :return: int list
    """
    l = []
    for i in range(largo):
        l.append(randint(inicio, fin))
    return l

def creadiccionario(lista):
    """
    Crea un diccionario con la frecuencia de cada
    componente de la lista
    :param lista: int list
    :return: dict
    """
    final = {}
    #for i in range(1, 6):
    for i in set(lista):
        final[i] = lista.count(i)
    return final

def inicio(inicio=1,fin=5):
    """
    Main del script
    :param inicio: int
    :param fin: int
    :return:
    """
    l=crealista(inicio,fin)
    print l
    final=creadiccionario(l)
    print final

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        inicio(int(sys.argv[1]),int(sys.argv[2]))
    else:
        inicio()
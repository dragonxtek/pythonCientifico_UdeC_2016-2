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

import random

class Dado:
    def __init__(self, sides=6,valor=0):
        if valor==0:
            self.valor=random.randint(1,sides)
        else:
            self.valor=valor
        self.caras=sides

    def lanzar_dado(self):
        self.valor=random.randint(1,self.caras)
        return self.valor

    def mostrar_lanzamiento(self):
        print "Has obtenido un ",str(self.valor)

    def __add__(self, other):
        if (self.valor+other.valor)%2==0:
            print "La suma de ambos lanzamientos es par"
        else:
            print "La suma de ambos lanzamientos es impar"

if __name__ == "__main__":
    dado1=Dado()
    # Guardamos el valor del lanzamiento en un objeto temporal
    lanzamiento=Dado(dado1.caras,dado1.lanzar_dado())
    dado1.mostrar_lanzamiento()
    # Se vuelve a lanzar el dado
    dado1.lanzar_dado()
    dado1.mostrar_lanzamiento()
    # Se suma el valor previo con el actual
    dado1+lanzamiento
    # Lanza 2 dados y suma sus valores
    #dado2 = Dado()
    #dado2.lanzar_dado()
    #dado2.mostrar_lanzamiento()
    #dado1+dado2



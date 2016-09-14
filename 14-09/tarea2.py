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

import sys

def factorial(num=5):
    """
    Calcula el factorial de un número
    :param num: int
    :return: int
    """
    total=1
    for i in xrange(1,num+1):
        total*=i
    return total

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        print "El factorial de ",sys.argv[1],"es",factorial(int(sys.argv[1]))

    else:
        num=int(raw_input("Ingrese un número: "))
        print "El factorial de ", num, "es", factorial(num)
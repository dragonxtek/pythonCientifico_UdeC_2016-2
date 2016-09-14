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

def printPrimos(max=1000):
    """
    Calcula los números primos hasta un valor máximo
    :param max: int
    :return: int list
    """
    primos=[]
    for i in range(1,max+1):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c+=1
        if c==0:
            primos.append(i)
    return primos

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        print printPrimos(int(sys.argv[1]))
    else:
        print printPrimos()
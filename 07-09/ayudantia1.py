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
"""
tarea1() solicita fecha en formato dd/mm/yyyy y guarda los valores en un diccionario
tarea2() solicita ingresar segundos y retorna la cantidad de dias,horas,minutos y segundos respectivos
"""


def tarea1(fecha='nan'):
    """
    tarea1() solicita fecha en formato dd/mm/yyyy y guarda los valores en un diccionario
    """
    if fecha == 'nan':
        fecha = raw_input('Ingrese fecha: ')
    # fecha='7/8/89'
    fecha_sep = fecha.split('/');
    final = {'dia': fecha_sep[0], 'mes': fecha_sep[1], 'año': fecha_sep[2]}
    print 'dia', final['dia'], 'mes', final['mes'], 'año', final['año']

def tarea2(segundos='nan'):
    """
    tarea2() solicita ingresar segundos y retorna la cantidad de dias,horas,minutos y segundos respectivos
    """
    if segundos == 'nan':
        segundos = int(raw_input('Ingrese segundos: '))
    # segundos=666
    dias = segundos / (60 * 60 * 24)
    r_dias = segundos % (60 * 60 * 24)
    horas = r_dias / (60 * 60)
    r_horas = r_dias % (60 * 60)
    minutos = r_horas / (60)
    r_minutos = r_horas % (60)
    segundos = r_minutos
    print 'dias', dias, '\n', 'horas', horas, '\n', 'minutos', minutos, '\n', 'segundos', segundos

# TODO using switch

if __name__ == "__main__":
    import sys
    if (len(sys.argv)==1):
        tarea1()
        print '\n'
        tarea2()
    if (len(sys.argv)==2):
        tarea1(sys.argv[1])
        print '\n'
        tarea2()
    if(len(sys.argv)==3):
        tarea1(sys.argv[1])
        print '\n'
        tarea2(int(sys.argv[2]))





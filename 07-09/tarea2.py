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

segundos=int(raw_input('Ingrese segundos: '))
dias=segundos/(60*60*24)
r_dias=segundos%(60*60*24)
horas=r_dias/(60*60)
r_horas=r_dias%(60*60)
minutos=r_horas/(60)
r_minutos=r_horas%(60)
segundos=r_minutos
print dias,horas,minutos,segundos
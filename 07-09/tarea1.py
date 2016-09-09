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

fecha=raw_input('Ingrese fecha: ')
#fecha='7/8/89'
fecha_sep=fecha.split('/')
final={'dia':fecha_sep[0],'mes':fecha_sep[1],'año':fecha_sep[2]}
print 'dia',final['dia'],'mes',final['mes'],'año',final['año']
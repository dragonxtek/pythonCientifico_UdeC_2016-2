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
from random import choice
import json

def frase():
    """
    Genera frases de forma aleatoria
    :return: string list
    """
    Sujeto=["tu madre","tu herman@","la gordis","el profe","la secreatria","el conserje"]
    Accion=["está durmiendo","se cayó","está borrach@","está estudiando","está manejando"]
    Lugar=["en el baño","en el subterraneo","en la cocina","en la sala","en la UdeC"]
    tmp= [Sujeto[randint(1,len(Sujeto))-1], Accion[randint(1,len(Accion))-1], choice(Lugar)]
    # Python append() removes utf-8 encoding
    # print json.dumps(tmp, ensure_ascii=False)
    return tmp

def list2str(lista):
    """
    Convierte una lista a un string
    :param lista: string list
    :return: string
    """
    string=""
    for i in range(len(lista)):
        string+=lista[i]+" "
    return string

if __name__ == "__main__":
    print list2str(frase())
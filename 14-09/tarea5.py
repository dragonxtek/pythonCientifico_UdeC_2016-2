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

from numpy import sort
from numpy import mean

# TODO agregar compatibilidad con tildes
texto="""Python was conceived in the late 1980s,[31] and its implementation began in
        December 1989[32] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI)
         in the Netherlands as a successor to the ABC language (itself inspired by SETL)
         [33] capable of exception handling and interfacing with the operating system
         Amoeba.[8] Van Rossum is Python's principal author, and his continuing central
         role in deciding the direction of Python is reflected in the title given to him
         by the Python community, benevolent dictator for life (BDFL)."""

def remueveCaracteresEspeciales():
    """
    Retorna un string que sólo posee letras (case-sensitive) y espacios
    :return: string
    """
    texto2=''
    for i in texto:
        if ord(i)==32 or (ord(i)<=122 and ord(i)>=97) or (ord(i)>=65 and ord(i)<=90):
            texto2+=i
    return texto2

def identificaPalabrasInicianMayuscula():
    """
    Retorna las palabras que comienzan con mayúscula
    :return: string list
    """
    palabrasMay=[]
    for i in texto3:
        if (ord(i[0])>=65 and ord(i[0])<=90):
            palabrasMay.append(i)
    return palabrasMay

def cuentaRepeticionesPalabra(palabra='es'):
    buscar=palabra.lower() #convierte la palabra a minúscula
    return textoMin.count(buscar)

#TODO retornar una lista en caso de existir varias palabras
def palabraModa():
    """
    Retorna la palabra más repetida del texto
    :return: string
    """
    palabrasUnicas = set(textoMin)
    contador = {}
    for i in palabrasUnicas:
        contador[i] = textoMin.count(i)
    freqValues = contador.viewvalues()  # obtiene una lista con las frecuencias
    freqValuesSorted = sort(list(freqValues))
    modaValue = freqValuesSorted[len(freqValuesSorted) - 1]
    return [key for key, value in contador.iteritems() if value == modaValue][0]    # busca la key asociada a modaValue

def promedioLetrasPorPalabra():
    """
    Retorna el promedio de letras por palabra del texto
    :return: float
    """
    cantidad=[]
    for i in texto3:
        cantidad.append(len(i))
    #return sum(cantidad)/float(len(cantidad))
    return mean(cantidad)


#Retorna la primera palabra encontrada que sea de largo máximo
#TODO retornar una lista en caso de existir varias palabras del mismo largo máximo
def palabraMasLarga():
    """
    Retorna la palabra más larga del texto
    :return: string
    """
    palabra=''
    for i in list(set(texto3)):
        if (len(i)>len(palabra)):
            palabra=i
    return palabra

def numeroVocalesTotal():
    """
    Retorna el número de vocales del texto
    :return: int
    """
    vocales=0
    for i in texto2.lower():
        if (ord(i)==97 or ord(i)==101 or ord(i)==105 or ord(i)==111 or ord(i)==117):
            vocales+=1
    return vocales


if __name__ == "__main__":
    texto2=remueveCaracteresEspeciales()
    texto3=texto2.split()               # convierte el texto a una lista
    textoMin = texto2.lower().split()   # convierte el texto a una lista en minúsculas
    print "Las palabras que comienzan con mayúscula son:",identificaPalabrasInicianMayuscula()
    print "La palabra Python aparece ",cuentaRepeticionesPalabra('Python')," veces"
    print "La palabra más repetida es:",palabraModa()
    print "La palabra más larga es:", palabraMasLarga()
    print "El promedio de letras por palabra es:",promedioLetrasPorPalabra()
    print "La cantidad de vocales en el texto es:",numeroVocalesTotal()
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

class Libro(object):
    def __init__(self):
        self.titulo="Sin nombre"
        self.autor="Anónimo"
        self.materia="Genérico"
        self.paginas=100
        self.precio=10000

    def ingresar_libro(self):
        self.titulo=raw_input("Ingrese Título del libro: ")
        self.autor=raw_input("Ingrese autor del libro: ")
        self.materia=raw_input("Ingrese materia del libro: ")
        while(1):
            self.paginas=int(raw_input("Ingrese páginas del libro: "))
            if self.paginas >0:
                break;
        while(1):
            self.precio = int(raw_input("Ingrese precio del libro: "))
            if self.precio > 0:
                break;

    def mostrar_libro(self):
        print
        print   "Título:\t\t",self.titulo,\
                "\nAutor:\t\t",self.autor,\
                "\nMateria:\t",self.materia,\
                "\nPáginas:\t",str(self.paginas),\
                "\nPrecio:\t\t",str(self.precio)

class Biblioteca(object):
    def __init__(self,nombre="Nombre de la Biblioteca",
                 ciudad="Ciudad de la bilioteca"):
        self.nombre=nombre
        self.ciudad=ciudad
        self.libros=[]  # Lista vacía
        self.cantidad=0

    def ingresar_libro(self,titulo="Sin nombre",precio=10000):
        tmp=Libro()
        #tmp.ingresar_libro()
        tmp.titulo=titulo
        tmp.precio=precio
        self.libros.append(tmp)
        self.cantidad+=1
        print "Libro ingresado"

    def eliminar_libro(self,nombre="Sin nombre"):
        if nombre != "Sin nombre":
            eliminar= nombre
        else:
            eliminar = raw_input("Ingrese libro a eliminar:")
        if self.existe_libro(eliminar)==0:
            print "Este libro no existe"
            return
        else:
            for i in self.libros:
                if(i.titulo==eliminar):
                    self.libros.remove(i)
                    self.cantidad-=1
                    print "Libro eliminado"


    def ordenar_precio(self):
        self.libros= sorted(self.libros,key= lambda x:x.precio,reverse=False)

    # todos los libros de la biblioteca
    def mostrar_biblioteca(self):
        for i in self.libros:
            print i.titulo

    def existe_libro(self,titulo="false"):
        if titulo != "false":
            buscar=titulo
        else:
            buscar=raw_input("Ingrese libro a buscar:")
        for i in self.libros:
            if(i.titulo==buscar):
                return 1
        return 0

    #ingresar titulo del libro a buscar
    def stock_disponible(self,titulo="false"):
        if self.existe_libro(titulo)==0:
            print "No hay stock"
        else:
            print "Hay stock"

if __name__ == "__main__":
    libro=Libro()
    #libro.ingresar_libro()
    #libro.mostrar_libro()
    #b=Biblioteca()
    #b.ingresar_libro()
    #b.ingresar_libro("lala",500)
    #b.eliminar_libro()
    #b.mostrar_biblioteca()
    #b.stock_disponible("Sin nombre")
    #b.stock_disponible("lala")



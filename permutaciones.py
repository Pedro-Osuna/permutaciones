#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:47:33 2020

@author: popscra
"""

"""
Este programa realiza las diferentes permutaciones, sin y con repeticion
que se dan en una palabra con sus caracteres, de no mas de 8 caracteres.

Calculo de el numero de permutaciones sin repeticion de una serie de 
elementos:
    P = Permutaciones
    n es el numero de elementos
                Pn = n! 
                
Calculo de el numero de permutaciones sin repeticion de una serie de 
elementos de forma circular (como ejemplo, al rededor de una mesa):
    P = Permutaciones
    n = es el numero de elementos
                Pn = (n-1)! 

Calculo de el numero de permutaciones de una serie de elementos con
elementos repetidos
    PR = Permutaciones con repeticion
    n  = es el numero de elementos
    a,b,... = cantidad de cada uno de los elementos que se repiten
                  a,b...       n!
                PR       = ----------
                  n         a!*b!*...
                
    Un ejemplo de la palabra 'GOOGLE' 
                                6!
                        PR =  -------
                               2!*2!
    un 2! es por dos letras repetidas la  G 
    el otro 2! por dos letras repetidas la O                                       
"""

"""
Este programa realiza las permutaciones de hasta solo 8 elementos,
tanto si tiene elementos con repeticion  como si no los tiene, 
ofreciendonos un listado de todas las posibles permutaciones.

  ====================== PROCESO =========================

Proceso que se ha seguido para realizar el modulo de visualizacion
de todas las permutaciones, tanto si se dan elementos sin repeticion como si 
si hay elementos repetidos.
No se contemplan Permutaciones circulares

El proceso parte de las diferentes palabras que podemos crear tomando:
la primera letra de la palabra a permutar, corremos todas
las demas hacia la izquierda y la que hemos tomado la ponemos la ultima.
Esto nos dara tantas palabras como cantidad de caracteres tiene la 
palabra dada a permutar y  cada una de las palabras empezara con uno de
los caracteres de la palabra dada en el orden encontrados.
Estas palabras las guardaremos en una tabla, y con cada una de ellas 
buscaremos las diferentes permutaciones posibles

De cada una de las palabras guardadas en la tabla buscamos las 
permutaciones posibles, siguiendo el siguiente proceso:
    .--Creamos las permutaciones de un solo caracter, guardamos en tabla T1
    .-Recorremos la palabra guardando cada caracter por separado en la
    tabla T1
     
    Creamos las permutaciones de dos caracteres, guardamos en tabla T2
    .-Recorremos la tabla T1.
    Cada elemento lo combinamos con cada una de las otras 
    letras, si alguna de las otras letras a combinar esta mas de una vez,
    solo la combinaremos una de las veces, la combinacion la añadiremos a la 
    tabla llamada T2 (por tener dos caracteres)
    Esto nos dara la tabla T2 conjunto de la permutacion de cada una de 
    las letras de la tabla T1 con todas las demas letras
    .-De la tabla obtenida T2 quitaremos todos los elementos que esten
    repetidos, dejando la tabla en el mismo orden sin los repetidos.
    (Utilizamos la funcion => del_duplicate(alist))
    
    .-- El proceso para completar las tablas (T3,T4,T5,T6,T7,T8)
    es identico a como se hace en el proceso explicado para completar la
    tabla T2, recorriendo la tabla enterior y por cada elemento hacer las
    permutaciones llenando en cada caso la tabla.
    
 Se rellenaran tantas tablas como letras tenga la palabra dada a buscar
 sus permutaciones.
 La tabla que contendra todas las permutaciones posibles de la palabra 
 sera aquella que su numero corresponda , con la cantidad de caracteres de la 
 palabra.
"""
# ===================     FUNCIONES ===================================
def del_duplicate(alist):
    """
    Funcion que nos borrar todos los elementos que se repiten de una
    lista manteniendo el orden de la misma.
    """
    seen = set()
    seen_add = seen.add
    return [x for x in alist if not (x in seen or seen_add(x))]


def imprimir(tabla):
    """
    Funcion que nos imprime por pantalla el resultado de todas las 
    permutaciones
    """
    y = 0
    #del_duplicate(tabla)
    for x in tabla:
        print(x,end=' ')
        y +=1
    print('\n ====== Cantidad de permutaciones: {} ======'.format(y))
    
# ===================   FIN FUNCIONES =================================

# Pedimos una palabra entre 2 y 8 caracteres ambos inclusive 
palabra = ''
lon = len(palabra)
while lon == 0 or lon > 6:
    palabra = input('Introduzca la palabra: ')
    lon = len(palabra)

#
tpalabra = []
tpalabra.append(palabra)

for x in range(lon-1) :
    """
    ponemos en una tabla las diferentes palabras que podemos crear. 
    Tomamos la primera letra de la palabra, corremos todas las demas
    hacia la izquierda y la que hemos tomado la ponemos la ultima.
    Esto nos dara una nueva palabra, y asi hasta hacerlo con todas las 
    letras de la palabra dada.
    Estas palabras, nos serviran para buscar las diferentes
    combinaciones posibles 
    """
    caract = palabra[0:1]
    palabra = palabra[1:]
    nueva_palabra = palabra + caract
    palabra = palabra + caract
    tpalabra.append(nueva_palabra)




#Modulo que nos genera todas las permutaciones
cant = 0
t1 = []  # guarda las permutaciones de un     solo caracter
t2 = []  # guarda las permutaciones de dos    caracteres
t3 = []  # guarda las permutaciones de tres   caracteres
t4 = []  # guarda las permutaciones de cuatro caracteres
t5 = []  # guarda las permutaciones de cinco  caracteres
t6 = []  # guarda las permutaciones de seis   caracteres
t7 = []  # guarda las permutaciones de siete  caracteres
t8 = []  # guarda las permutaciones de ocho   caracteres
for palabra in tpalabra:
    lon=len(palabra)
    
    # llenamos la tabla T1
    if lon > 0:
        for letra in palabra:
            t1.append(letra)

    # llenamos la tabla T2
    if  lon > 1:    
        """ recorremos todos los elementos de T2 """
        for letras1 in t1:
            nueva_palabra = palabra
            """ Recorremos todos los caracteres de elemento tradado de T1
            para dejar en nueva_palabra la palabra sin caracteres
            repetidos """
            for letra  in letras1:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            """ rellenamos la tabla T2 con las permutaciones 
            de dos caracteres """
            for letra in nueva_palabra:
                t2.append(letras1 + letra)
            """ quitamos los elementos repetidos de la tabla dejandola
            en el mismo orden """
            t2 = del_duplicate(t2)
    
    if  lon > 2:    
        for letras2 in t2:
            nueva_palabra = palabra
            for letra  in letras2:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            for letra in nueva_palabra:
                t3.append(letras2 + letra)
            t3 = del_duplicate(t3)
    if lon == 3:
        tabla = t3

    if  lon > 3:    
        for letras3 in t3:
            nueva_palabra = palabra
            for letra  in letras3:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            for letra in nueva_palabra:
                t4.append(letras3 + letra)
            t4 = del_duplicate(t4)
    if lon == 4:
        tabla = t4
    
    if  lon > 4:    
        for letras4 in t4:
            nueva_palabra = palabra
            for letra  in letras4:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            for letra in nueva_palabra:
                t5.append(letras4 + letra)
            t5 = del_duplicate(t5)
    if lon == 5:
        tabla = t5
    
    if  lon > 5:    
        for letras5 in t5:
            nueva_palabra = palabra
            for letra  in letras5:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            for letra in nueva_palabra:
                t6.append(letras5 + letra)
            t6 = del_duplicate(t6)
    if lon == 6:
        tabla = t6
    
    if  lon > 6:    
        for letras6 in t6:
            nueva_palabra = palabra
            for letra  in letras6:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            for letra in nueva_palabra:
                t7.append(letras6 + letra)
            t7 = del_duplicate(t7)
    if lon == 7:
        tabla = t7
    
    if  lon > 7:    
        for letras7 in t7:
            nueva_palabra = palabra
            for letra  in letras7:
                if letra in nueva_palabra:
                    num = nueva_palabra.find(letra)
                    if num == 0:
                        nueva_palabra = nueva_palabra[num+1:]
                    elif num == lon:
                        nueva_palabra = nueva_palabra[:num-1]
                    else:
                        nueva_palabra = nueva_palabra[:num] + nueva_palabra[num+1:]
            for letra in nueva_palabra:
                t8.append(letras7 + letra)
            t8 = del_duplicate(t8)
    if lon == 8:
        tabla = t8

imprimir(tabla)
    

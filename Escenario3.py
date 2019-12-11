# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:39:00 2019

@author: Andres Losada
"""


import sys
import os

os.system("clear")

numeroHabitantes = [33000000, 230000000, 44000000]
costoObjetivo = [0.7, 1, 0.6, 0.2, 0.1]
porcentajeSexo = [0.62, 0.38]
porcentajeHablantes = [0.52, 0.16]
porcentajeDentroDeNicho = [0.03, 0.013]
costoUbicacion = [20/1000, 28/1000]
costoPorImpresion = [66/1000, 1/1000, 10/1000]
presupuesto = 6400

'''
#Habitantes por Pais con Facebook
numeroHabitantes[1] = 33000000  #Colombia
numeroHabitantes[2] = 230000000 #E.E.U.U.
numeroHabitantes[3] = 44000000  #UK

#Costo Objetivos
costoObjetivo[1] = 0.7   #Engagement
costoObjetivo[2] = 1   #Brand Awareness
costoObjetivo[3] = 0.6 #Traffic
costoObjetivo[4] = 0.2 #Lead Generation
costoObjetivo[5] = 0.1   #Conversions

#Porcentaje de Cada Sexo con Facebook
porcentajeSexo[1] = 0.62
porcentajeSexo[2] = 0.38

#Porcentaje de Hablantes 
porcentajeHablantes[1] = 0.52 #Ingles
porcentajeHablantes[2] = 0.16 #Español

#Porcentaje Dentro De Nicho
porcentajeDentroDeNicho[1] = 0.03 #Viajero
porcentajeDentroDeNicho[2] = 0.013 #High Tech

#Costo por Ubicacion
costoUbicacion[1] = 20/1000 #Facebook
costoUbicacion[2] = 28/1000 #Instagram

#Costo por Impresion en dolares
costoPorImpresion[1] = 66/1000 #Colombia
costoPorImpresion[2] = 1/1000 #E.E.U.U.
costoPorImpresion[3] = 10/1000 #UK
'''

maximo = 0 #Indice del Arreglo de máximos
estadoMaximo = [] #Indice dle arreglo de estados
estados = []
respuestas = []

def poblacion(p, s, i, n):
    return (numeroHabitantes[p] * porcS(s) * porcIyN(i,n))

def porcS(s):
    return porcentajeSexo[s]

def costosExtra(u, o, p):
    return costoPorImpresion[p] * (costoObjetivo[o]) * (costoUbicacion[u])

def porcIyN(i, n):
    return porcentajeHablantes[i] * porcentajeDentroDeNicho[n]


for p in range(0, len(numeroHabitantes)):
    for o in range(0, len(costoObjetivo)):
        for s in range(0, len(porcentajeSexo)):
            for n in range(0, len(porcentajeDentroDeNicho)):
                for u in range(0, len(costoUbicacion)):
                    for i in range(0, len(porcentajeHablantes)):
                        if(i == 0):
                            resAct = poblacion(p,s,i,n) * presupuesto * costosExtra(u,o,p)
                            respuestas = respuestas + [resAct]
                            estados = estados + [p, o, s, n, u, i]
                            if resAct > maximo:
                                maximo = resAct
                                estadoMaximo = [p, o, s, n, u, i]

                        

print(maximo)
print(estadoMaximo)

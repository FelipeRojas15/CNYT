import sys
  
from math import atan as arcota,sin,cos
##import numpy as n

def suma(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    return complex(float(a1+a2),float(b1+b2))
def resta(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    return complex(float(a1-a2),float(b1-b2))
def multiplicacion(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    return complex(float((a1*a2)-(b1*b2)),float((a1*b2)+(a2*b1)))
def division(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    
    return (round((a1*a2+b1*b2)/((a2)**2+(b2)**2),3),round(((a2*b1)-(a1*b2))/((a2)**2+(b2)**2),3))
                               
    
def conjugado(tuplaA):
    a1,b1 = tuplaA[0],tuplaA[1]
    return complex(float(a1),float(b1*-1))
def modulo(tuplaA):
    a1,b1 = tuplaA[0],tuplaA[1]
    return float((a1**2+b1**2)**0.5)
def polar(tuplaA):
    lista = []
    a1,b1 = tuplaA[0],tuplaA[1]
    z = round(modulo(tuplaA),3)
    angulo = round(arcota(b1/a1),3)
    lista.append(round(z,4))
    lista.append(round(angulo,4))
    tupla= tuple(lista)
    
    return tupla

def cartesiana(tuplaA):
    lista =[]
    modulo,direccion = tuplaA[0],tuplaA[1]
    a = modulo*cos(direccion)
    b = sin(direccion)
    lista.append(a)
    lista.append(b)
    tupla = tuple(lista)
    return tupla

def fase(tuplaA):
    
    a1,b1 = tuplaA[0],tuplaA[1]
    angulo = arcota(b1/a1)
    return round(angulo,3)


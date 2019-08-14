import sys
  
from math import atan as arcota,sin,cos
import numpy as n

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
    return complex(tupla)

def fase(tuplaA):
    
    a1,b1 = tuplaA[0],tuplaA[1]
    angulo = arcota(b1/a1)
    return round(angulo,3)
def main():
    print("Escriba la primera tupla: ")
    tuplaA = list(map(int,sys.stdin.readline().strip().split(",")))
    print("Escriba la segunda tupla: ")
    tuplaB = list(map(int,sys.stdin.readline().strip().split(",")))
    tuplaA = tuple(tuplaA)
    tuplaB = tuple(tuplaB)
    print("La suma es: ",suma(tuplaA,tuplaB))
    print("La resta es: ",resta(tuplaA,tuplaB))
    print("La multiplicacion es: ",multiplicacion(tuplaA,tuplaB))
    print("La division es: ", division(tuplaA,tuplaB))

    print("El conjugado de la primera tupla es: " ,conjugado(tuplaA))
    print("El conjugado de la segunda tupla es: ", conjugado(tuplaB))      
    
    print("El modulo de la primera tupla es: ", modulo(tuplaA))
    print("El modulo de la segunda tupla es: ", modulo(tuplaB))

    

    print("La forma polar para la primera tupla es: ", polar(tuplaA))
    print("La forma polar para la segunda tupla es: ", polar(tuplaB))

    print("La forma cartesiana para la primera tupla es: ", cartesiana(polar(tuplaA)))
    print("La forma cartesiana para la segunda tupla es: ", cartesiana(polar(tuplaB)))
                                    
    
    print("La fase o direccion que tiene la primera tupla es:  ", fase(tuplaA))
    print("La fase o direccion que tiene la segunda tupla es:  ", fase(tuplaA))
main()

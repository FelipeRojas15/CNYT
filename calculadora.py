import sys
  
from math import atan as arcota,sin,cos,pi,atan2
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
    try:
        return (round((a1*a2+b1*b2)/((a2)**2+(b2)**2),3),round(((a2*b1)-(a1*b2))/((a2)**2+(b2)**2),3))
    except ZeroDivisionError:print("No se puede dividir entre zero")                           
    
def conjugado(tuplaA):
    a1,b1 = tuplaA[0],tuplaA[1]
    return float(a1),float(b1*-1)
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
    b = modulo*sin(direccion)
    lista.append(a)
    lista.append(b)
    tupla = tuple(lista)
    return tupla

def fase(tuplaA):
    
    a1,b1 = tuplaA[0],tuplaA[1]
    angulo = atan2(b1/a1)
    return round(angulo,3)

def polarGrados(tupla):
    
    a1,b1 = tupla[0],tupla[1]
    modu = modulo(tupla)
    grado = atan2(b1,a1)
    grado = (grado*180)/pi
    
    return (round(modu,3),round(grado,3))
    
#✴✴✴✴✴✴✴✴✴✴✴✴ VECTORES Y MATRICES ✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴

def sumaDeVectores(vectorA,vectorB):
    if len(vectorA) != len(vectorB):
        return "Suma invalida"
    sumax = []
    for i in range(len(vectorB)):
        sumax.append(suma(vectorA[i],vectorB[i]))
    return sumax

def restaaDeVectores(vectorA,vectorB):
    if len(vectorA) != len(vectorB):
        return "Suma invalida"
    restax = []
    for i in range(len(vectorB)):
        restax.append(resta(vectorA[i],vectorB[i]))
    return restax



def multiplicacionVectorEscalar(vector,escalar):
    result =[]
    for i in range(len(vector)):
        result.append(multiplicacion(vector[i],(escalar,0)))
    return result

def sumaMatrices(matrizA,matrizB):
    if len(matrizA) != len(matrizA)or len(matrizA[0]) != len(matrizA[0]):
        return "Suma invalida"
    result = []
    for i in range(len(matrizA)):
        result.append(sumaDeVectores(matrizA[i],matrizB[i]))
    return result

def restaMatrices(matrizA,matrizB):
    if len(matrizA) != len(matrizA)or len(matrizA[0]) != len(matrizA[0]):
        return "Resta invalida"
    result = []
    for i in range(len(matrizA)):
        result.append(restaDeVectores(matrizA[i],matrizB[i]))
    return result

def multiplicacionMatrizEscalar(matrizA,vector):
    result =[]
    for i in range(len(vector)):
        result.append(multiplicacionVectorEscalar(matrizA[i], escalar))
    return result

def matrizTranspuesta(matriz):
    transpuesta =[]
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)
    return transpuesta

def matrizConjugada(matriz):
    conjugada = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[0])):
            fila.append(matriz[i][j])
        conjugada.append(conjugado(fila))
    return conjugada


def matrizAdjunta(matriz):
    return matrizTranspuesta(matrizConjugada(matriz))

def multiplicacionMatrices(matrizA,matrizB):
    filasB = len(matrizB)
    columnasA = len(matrizA[0])
    if filasB == columnasA:
        filas = len(matrizA)
        columnas = len(matrizB[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(matrizB)):
                    m = multiplicacion(matrizA[i][k], matrizB[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:
        
        raise 'La multiplicación de matrices no está definida para estas matrices'


#    #   #     PRUEBAS PARA INCORPORAR AL ARCHIVO .TEST

"calculadora.sumaDeVectores([(8,3),(-1,-4),(0,-9)],[(8,-3),(2,5),(3,0)])"












    

import sys
#import numpy as np
#import matplotlib.pyplot as plt
from math import atan as arcota,sin,cos,pi,atan2
##import numpy as n

def suma(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    return (float(a1+a2),float(b1+b2))
def resta(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    return (float(a1-a2),float(b1-b2))
def multiplicacion(tuplaA,tuplaB):
    a1,b1,a2,b2 = tuplaA[0],tuplaA[1],tuplaB[0],tuplaB[1]
    return (float((a1*a2)-(b1*b2)),float((a1*b2)+(a2*b1)))
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

def restaDeVectores(vectorA,vectorB):
    if len(vectorA) != len(vectorB):
        return "Suma invalida"
    restax = []
    for i in range(len(vectorB)):
        restax.append(resta(vectorA[i],vectorB[i]))
    return restax



def multiplicacionVectorEscalar(vector,escalar):
    result =[]
    for i in range(len(vector)):
        result.append(multiplicacion(vector[i],(escalar)))
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
    for i in range(len(matrizA)):
        result.append(multiplicacionVectorEscalar(matrizA[i], vector))
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
            fila.append(conjugado(matriz[i][j]))
        conjugada.append(fila)
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
def multiplicacionMatricesNormales(matriz1,matriz2):
    '''Entran 2 matrices, una de M x I, la otra de I X N, retorna
        la multiplicacion de lamatriz1 por la matriz 2 de dimension M X N'''
    if (len(matriz1) != len(matriz2[0])): raise 'La multiplicación de matrices no está definida para estas matrices'
    aux = []
    for i in range(len(matriz1[0])):
        aux.append( [None] * len(matriz2))
    for i in range(len(matriz1[0])):
        for j in range(len(matriz2)):
            summ = 0
            for k in range(len(matriz2[0])):
                summ += matriz1[i][k][0]*matriz2[j][k]
            aux[i][j] = summ
    return aux
def productoInternoVectores(vector1,vector2):
    if len(vector1) != len(vector2):
        raise 'Los vectores no tienen la misma longitud, su producto interno no esta definido'
    aux = (0,0)
    for i in range(len(vector1)): 
        aux = suma(aux,multiplicacion(vector1[i],vector2[i]))
    return aux;





def moduloVector(vector):
    aux = 0
    for i in vector:
        aux += modulo(i)**2
    return round(aux**0.5,2)




def distanciaEntreVectores(vector1,vector2):
    if len(vector1) != len(vector2):
        raise 'Los vectores no tienen la misma longitud, su producto interno no esta definido'
    return moduloVector(restaDeVectores(vector1,vector2))



        
def esHermitiana(matriz):
    if len(matriz) != len(matriz[0]):
        raise 'False'
    return matriz == matrizAdjunta(matriz)




def esUnitaria(matriz):
    if len(matriz) != len(matriz[0]):  raise 'False'
    i = [[(float(0),float(0)) for w in range(len(matriz))]for j in range(len(matriz))]
    for k in range(len(i)):
        i[k][k] = (float(1),float(0))
    return multiplicacionMatrices(matriz,matrizAdjunta(matriz)) == multiplicacionMatrices(matrizAdjunta(matriz),matriz) == i




def productoTensor(matriz1,matriz2):
    aux = []
    subLista = []
    conta = len(matriz2)
    for i in matriz1:
        valorB = 0
        valorA = 0
        while valorA < conta:
            for num1 in i:
                for num2 in matriz2[valorB]:
                    subLista.append(multiplicacion(num1,num2))
            aux.append(subLista)
            subLista = []
            valorA +=1
            valorB += 1
    return aux
#    #   #     PRUEBAS PARA INCORPORAR AL ARCHIVO .TEST

"calculadora.sumaDeVectores([(8,3),(-1,-4),(0,-9)],[(8,-3),(2,5),(3,0)])"


def marbels(matrizAdj, estadoInicial, clicks):
    '''Se simula el experimento de  las canicas despues de varios clicks'''
    while clicks > 0:
        clicks -= 1
        aux = []
        for i in range(len(matrizAdj)):
            sume = (0,0)
            for j in range(len(estadoInicial)):
               sume = suma(sume,multiplicacion(estadoInicial[j],matrizAdj[i][j]))
            aux.append(sume)
        estadoInicial  = aux
        '''
    labels = [  'Pto. '+ str(i) for i in range(len(matrizAdj))]
    estado = [ c[0] for c in estadoInicial]
    index = np.arange(len(labels))
    plt.bar(index, estado)
    plt.xlabel('Estados')
    plt.ylabel('Valores')
    plt.xticks(index, labels, rotation=30)
    plt.title('Evolucion del sistema')
    plt.show()'''
    return aux





def ensamble(sistemaA, estadoA, sistemaB, estadoB, clicks):
    '''Ensamble de dos sistemas'''
    
    sistema = productoTensor(sistemaA, sistemaB)
   
    estados = productoTensor([estadoA], [estadoB])
   
    return marbels(sistema, estados[0], clicks)
    


def doble_rendija(num_rendijas, num_blancos_pared, vector_probabilidad):
    '''Realiza el experimento de rendijas multiples con probabilidad ajustable'''
    
    num_paredes = num_rendijas + 1
    num_nodos = 2 * num_rendijas + num_paredes * num_blancos_pared + 1
    num_blancos_rendija = len(vector_probabilidad)
    matriz_sistema = [[(0, 0) for j in range(num_nodos)]for i in range(num_nodos)]
    posicion = 0
    for i in range(1, num_rendijas + 1):
        matriz_sistema[i][0][0] = 1/(num_rendijas**(1/2))
        posicion = i
    for i in range(1, num_rendijas + 1):
        for j in range(posicion, posicion + num_blancos_rendija + 1):
            matriz_sistema[j][i] = vector_probabilidad[i-1]
            
        
    return matriz_sistema














    

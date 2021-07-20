
# Matrices o vectores bidimensionales

# En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

# Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
# Esta librería está por fuera del alcance de este curso pero puedes investigarla.

# Veamos un ejemplo:

""" def ejemplo1():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    print(a)

ejemplo1()

#O podemos recorrer todos los elementos e imprimir como una matriz
def ejemplo2():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

ejemplo2() """

#Actividad 1
#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.


import random
def s13():
    n = int(input("fila: "))
    m = int(input("Colunas: "))
    matrix = []
    for i in range(n):
        matrix.append([0]*m)
    mini = 10
    maxi = 99
    vmin = maxi
    vmax = mini
        
    for i in range(n):
        for j in range(m):
            matrix[i][j] = random.randint(mini,maxi)
        
            if (matrix[i][j] < vmin):
                vmin = matrix[i][j]
                posmin = (i+1, j+1)

            if (matrix[i][j] > vmax):
                vmax = matrix[i][j]
                posmax =(i+1, j+1)
    print()
    print(f"El mayor {vmax} esta en la posicion {posmax} y el menor {vmin} esta en la posicion {posmin}")
    for i in matrix:
        print(i)
s13()

#Actividad 2
#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.


def matrizescalar():
    matrixinicial = [[4,5,6],[10,11,12],[19,20,21]]
    escalar = 7
    matrixnueva = []

    for i in range(len(matrixinicial)):
        fila = matrixinicial[i]
        nuevafila = []
        for j in range(len(fila)):
            nuevafila.append(matrixinicial[i][j]*escalar)
        matrixnueva.append(nuevafila)
    print(matrixnueva)

matrizescalar()
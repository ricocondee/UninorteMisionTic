# Funciones con listas

# Aquí van algunas funciones útiles cuando trabajamos con listas.

#     remove(x) - remueve el primer valor X de la lista
#     pop([i]) - remueve el valor en la posición i. pop() remueve el último valor de la lista
#     len(x) - permite calcular el tamaño de una lista


#Actividad 1

#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden

#-------------------------------------------------SOLUCION-----------------------------------------------------------------------------------

import random # importo la libreia "random" para trabajar con numeros aleatorios
rango = range(1,20) # asigno el rango a la variable con la funcion "range"
lista = random.sample(rango, 6) #le digo agrege solo N numeros aleatorios del rango a la lista
def mayor(x):
    mayor = 0           #--------------------------------
    for i in x:                                        #
        if i > mayor:                                  #----> Esto se puede reemplazar por la funcion max ejemplo: mayor = max(lista)
            mayor = i   #------------------------------
    print(f"El mayor numero es: {mayor}")

def primos(x):
    primis = []
    for i in lista:
        div = 0
        for j in range(2,i+1):
            if i % j == 0:
                div +=1
        if div == 1:
            primis.append(i)
    print(f"Los numeros primos son: {primis}")

def orden(x):
    x.sort() # ordena los valores de forma acendente
    print(f"La lista ordenada {x}")

print(lista)
mayor(lista)
primos(lista)
orden(lista)
# por ultimo imprimo la lista y llamo a todos los def para que funcione el codigo
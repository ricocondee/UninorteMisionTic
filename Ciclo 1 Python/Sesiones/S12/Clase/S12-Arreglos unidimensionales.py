""" def insercion():
    print()
    print("----- Inserción en lista ordenada -----")
    Vector = [2,5,15,20,35,50]
    print("Lista original: ",Vector)
    pos = 0
    numero = int(input("Número a insertar : "))
    while(pos <= len(Vector)-1 and Vector[pos] < numero):
        pos += 1
    Vector.append(0)
    for i in range(len(Vector)-1, pos-1, -1):
        Vector[i] = Vector[i-1]
    Vector[pos] = numero
    print("Nueva lista ordenada: ",Vector) 


def insercion_desordenado_fijo():
    print()
    print("----- Inserción en lista desordenada fija -----")
    Vector = [89,23,0,15,90]
    print(Vector)
    posicion = int(input("Posición a insertar: "))
    if posicion-1 <= len(Vector)-1:
        numero = int(input("Numero a insertar : "))
        i = 0
        while(i <= len(Vector)-1):
            if i == posicion-1:
                Vector[i] = numero
                break
            i += 1
        print(Vector)
    else:
        print("Fuera de rango")

def insercion_desordenado_variable():
    print()
    print("----- Inserción en lista desordenada variable -----")
    Vector = [89,23,0,15,90]
    print(Vector)
    pos = int(input("Posición a insertar: "))
    if pos-1 <= len(Vector)-1:
        numero = int(input("Numero a insertar : "))
        i = 0
        while(i <= len(Vector)-1):
            if i == pos-1:
                Vector.append(0)
                break
            i += 1
        pos = i
        aux = Vector[pos]
        for i in range(len(Vector)-1, pos-1, -1):
            Vector[i] = Vector[i-1]
        Vector[pos] = numero
        print(Vector)
    else:
        print("Fuera de rango, no se puede insertar el número")


#Programa principal

op = 0
while(op != 4):
    print("1. Inserción en vector ordenado")
    print("2. Inserción en vector desordenado fijo")
    print("3. Inserción en vector desordenado variable")
    print("4. Salir")
    op = int(input("Elija la opción: "))
    if op == 1:
        insercion()
    elif op == 2:
        insercion_desordenado_fijo()
    elif op == 3:
        insercion_desordenado_variable()
    elif op == 4:
        print("Gracias por utilizar el sistema")
    else:
        print("Elija una opción válida")
 """

#Actividad 1

#Escribamos un programa que nos permita crear con una lista de 6 números aleatorios entre 1 y 20, 
#y luego creemos tres funciones que reciban la lista como parámetro de la siguiente forma:
#
#    mayor(x) - Una función que imprima el número mayor valor de una lista x
#    primos(x) - Una función que imprima los números de la lista que son números primos
#    orden(x) - Una función que ordene los datos de una lista x ascendentemente y la imprima en orden


#Solución

""" def mayor(x):
    mayor = 0
    for i in x:
        if i > mayor:
            mayor = i
    print(f"El mayor es: {str(mayor)}")

def primos(x):
    print("Primos de la lista")
    listaPrimos = []
    for i in x:
        div = 0
        for j in range(2,i+1):
            if (i % j == 0):
                div += 1
        if div == 1:
            listaPrimos.append(i)
    print(listaPrimos)

def orden(x):
    x.sort()
    print("La lista ordenada:",x)

#Programa principal
def principal():
    import random
    lista=[]
    for i in range(6):
        lista.append(random.randint(1,20))
    print(lista)
    mayor(lista)
    primos(lista)
    orden(lista)

principal() """


#Programa que lea la cantidad de datos en una lista aplicando las funciones de listas

#Solución

import os
nombres = []

def limpiarpantalla():
    os.system("cls")
    print("La cantidad de datos en la lista son: ",len(nombres))
    print(nombres)

def agregar():
    nom = str(input("Ingrese un nombre: "))
    nombres.append(nom)
    menuppal()

def mostrar():
    print(nombres)

def removerxnombre():
    nom = str(input("Ingrese nombre a remover: "))
    nombres.remove(nom)
    menuppal()

def removerxposicion():
    pos = int(input("Ingrese la posición de la persona a remover: "))
    nombres.pop(pos)
    menuppal()

def mostrarxposicion():
    pos = int(input("Ingrese la posición de la persona a consultar: "))
    print("En la posición ",pos," se encuentra ",nombres[pos])
    p = str(input("<ENTER>"))
    menuppal()

def menuppal():
    limpiarpantalla()
    menu = int(input("1. Agregar\n2. Mostrar\n3. Remover x nombre\n4. Remover x posición\n5. Tamaño de la lista\n6. Orden ascendente\n7. Orden descendente\n8. Consultar x posición\n9. Salir\nEligue un opcion: "))
    if menu == 1:
        agregar()
    elif menu == 2:
        mostrar()
    elif menu == 3:
        removerxnombre()
    elif menu == 4:
        removerxposicion
    elif menu == 5:
        print("La cantidad de datos en la lista son: ",len(nombres))
        menuppal()
    elif menu == 6:
        nombres.sort()
        menuppal()
    elif menu == 7:
        nombres.sort(reverse=True)
        menuppal()
    elif menu == 8:
        mostrarxposicion()
    elif menu == 9:
        print("Gracias por utilizar el sistema")

menuppal()

        
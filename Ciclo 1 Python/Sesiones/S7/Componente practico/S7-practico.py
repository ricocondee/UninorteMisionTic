"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

Por ejemplo:
"""

""" def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        i += 1
ejemplo1() """

# Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número.

def actividad1(num = 100):
    c1 = 0
    c2 = 0
    pares = []
    while c1 < num:
        if c2 % 2 ==0:
            pares.append(c2)
            c1 =+1
        c2 =+1
    return pares
n = int(input("Ingresa un numero: "))
if n > 0:
    pares = actividad1(n)
    print(pares)
    print("Cantidad de pares", len(pares))
else:
    print(",m klk")
     

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario.

#actividad2()    
    

def actividad3():
    print("actividad3")
    #Escribe el código que solicite números al usuario hasta que éste ingrese -1.
    #Cuando se ingrese -1, el programa debe imprimir el promedio de todos los números ingresados hasta ese momento (sin contar con el -1).

#actividad3()
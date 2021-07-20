"""
Mientras Que

Como vimos anteriormente, en Python, el ciclo Mientras Que se maneja con "while". 

La opción break, puede parar el ciclo aunque la condición sea real. Por ejemplo:
"""

def ejemplo1():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1 
ejemplo1()

def actividad1():
    print("actividad1")
    # Continuemos integrando los conceptos que hemos visto hasta el momento. 
    # Ahora vamos a elaborar un algoritmo que pida un número al usuario, e imprima todos los números pares desde 2 hasta el número pero que termine el proceso si llega al 10.

# Para ejecutar cada actividad, debes quitar el comentario a la línea que llama el bloque de código
#actividad1()


"""
La opción continue, puede continuar el ciclo y saltarse cuando sea verdadera. Por ejemplo:
"""
def ejemplo2():
    i = 1
    while i < 6:
        if i == 3:
            i += 1 
            continue
        print(i)
        i += 1 

#ejemplo2()

def actividad2():
    print("actividad2")
    #Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario pero saltarse si el digito es 4.

#actividad2()
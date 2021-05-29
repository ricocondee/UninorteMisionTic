
# Cada ejemplo y actividad será definida como un bloque independiente.
# Si-Sino-Finsi
# Recuerda que los condicionales múltiples y anidados nos permiten evaluar múltiples casos. 
# El condicional Si-Sino-Si-Finsi tiene la siguiente estructura:

#     Si (condición) Entonces
#         instrucción(es)
#     Sino Si
#         instrucción(es)
#     Fin Si

# En Python, esto se escribe un poco diferente y la estructura general depende de las tabulaciónes. 
# Por ejemplo:

""" def ejemplo1(): #se define con la palabra reservada "def" una funcion, ()<--- aqui se le asigna un parametro opcional
    x = int(input("Por favor ingresa un número: "))
    if x < 0:
        print('El número es Negativo')
    elif x > 0:
        print('El número es positivo')
    elif x == 0:
        print('El número es cero')
ejemplo1() #se manda a llamar la funcion
 """

 #               Actividades

 # Actividad 1
 # Escribe el código que imprima un comando dada la luz del semáforo
        #Verde = Siga
        #Amarillo = Precaución
        #Rojo = Pare

""" def actividad1():
    verde = "siga"
    amarillo = "Precaucion"
    rojo = "pare"
    luz = input("Ingresa el color del semaforo: ")
    if luz == "verde":
        print(verde)
    elif luz == "amarillo":
        print(amarillo)
    elif luz == 'rojo':
        print(rojo)
    else:
        print("Solo pueden ser verde, amarillo o rojo")
actividad1() """
    
 #Escribe el código que basado en la actividad 1 y una variable que nos indica si hay peaton o no (hayPeaton), 
 # imprima:
        #Verde -------- Si hay peaton - Pare, Sino - Siga
        #Amarillo ----------- Si hay peaton - Pare, Sino - Precaución
        #Rojo = Pare
""" def actividad2():
    verde = "siga"
    amarillo = "Precaucion"
    rojo = "pare"
    luz = input("Ingresa el color del semaforo: ")
    haypeaton = input("Hay peaton?: ")
    if luz == "verde" and haypeaton == "si":
        print(f"Si hay peaton {rojo}")
    elif luz == "verde" and haypeaton == "no":
        print(verde)
    elif luz == "amarillo" and haypeaton == "si":
        print(f"Si hay peaton {rojo}")
    elif luz == "amarillo" and haypeaton == "no":
        print(amarillo)
    elif luz == 'rojo':
        print(rojo)
    else:
        print("Solo pueden ser verde, amarillo o rojo\nSi o no")
   
actividad2() """

#Escribe el código para dos numeros a y b, el usuario va a seleccionar una opcion: 
        #1 para sumar, 2 para multiplicar, 3 para restar (a-b) y 4 para dividir (a/b) y 
        #retornar el resultado de la operación indicada.

def actividad3():
    numa = int(input("Ingresa el numero a: "))
    numb = int(input("Ingresa el numero b: "))
    suma = numa+numb
    multi = numa*numb
    resta = numa-numb
    div = numa/numb
    def menu():
        opcion = int(input("\n   Opciones\nSumar [1]\nMultiplicar [2]\nRestar [3]\nDividir [4]\nElige una opcion: "))
        if opcion == 1:
           print(f"{numa} + {numb}: = {suma}")
        elif opcion == 2:
           print(f"{numa} x {numb}: = {multi}")
        elif opcion == 3:
            print(f"{numa} - {numb}: = {resta}")
        elif opcion == 4:
            print(f"{numa} ÷ {numb}: = {round(div,2)}")
        else:
            print("Escoge una opcion valida")
    menu()

actividad3()
    
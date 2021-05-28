# Diseñar 3 opciones:
#
#   1. Leer un número de 4 dígitos, mostrar el dígito mayor e 
#      informar si es par o impar.
#   2. Leer dos números de 3 dígitos cada uno, formar un tercer número 
#      con el mayor del primero y el menor del segundo.
#   3. Leer un número de 3 dígitos y formar el mayor número posible 
#      con sus cifras.
#   
# Luego crea un menú con las tres opciones.

def funcion1():
    num = int(input("Cifra: "))
    if num % 10:
        num = num % 1000 and num % 100 and num %10
        num2 = num
        print(f"El mayor dígito es {num2}" ) 
funcion1()

""" def funcion2():
    #Escribe el código de la segunda opción aquí
    print("El nuevo dígito es " )

def funcion3():
    #Escribe el código de la tercera opción aquí
    print("El nuevo dígito es ")

if __name__ == "__main__":
    #Escribe el código aquí para que el usuario seleccione una opción. Llamas cada opción como
    #funcion1()
    #funcion2()
    #funcion3() """
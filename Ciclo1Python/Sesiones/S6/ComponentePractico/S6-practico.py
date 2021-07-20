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

def menu():
    opcion = int(input(""""
                    _______________________________________
                   |               OPCIONES                |
                   |_______________________________________|
                   | 1. Mayor numero y si es par o impar   |
                   |_______________________________________|
                   | 2. Numero formado con el mayor y menor|
                   |_______________________________________|
                   | 3. Maximo numero posible              |
                   |_______________________________________|
                   | Elije una opcion: | """))
    print()
    if opcion == 1:
        def mayor(x):
            num = []
            for i in x:
                num.append(int(i))
            if max(num) % 2 == 0:
                print(f"El mayor numero es: {max(num)}, y es par.")
            else:
                print(f"El mayor numero es: {max(num)}, y es impar.")
        cif = input("Numero de cuatro digitos: ")
        mayor(cif)
    elif opcion == 2:
        def tres(y):
            tres1 = []
            tres2 = []
            for i in y:
                tres1.append(int(i))
            for j in num2:
                tres2.append(int(j))
            print(f"El nuevo numero es: {max(tres1)}{min(tres2)}")
        num = input("Numero de tres digitos:")
        num2 = input("Otro numero de tres digitos: ")
        tres(num)
    elif opcion == 3:
        def maxpo():  
            num = input("Numero de tres digitos: ")
            num = list(num)
            numlst = list()
            for i in range(3):
                maxi = num.index(max(num))
                numlst.append(num[maxi])
                num.pop(maxi)
            maxnumpo = int(numlst[0]+ numlst[1]+ numlst[2])
            print(f"Nuevo numero {maxnumpo}")
        maxpo()
    else:
        print("Ingresa una opcion valida")
menu()
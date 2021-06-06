# Actividad 1 ESTRUCTURA SECUENCIAL

# Hallar el área de un círculo. 𝐴=𝜋𝑟2
def A():
    circulo = float(input("Ingresa el Radio: "))
    areaf = 3.1416*circulo**2
    print(f"El area del circulo es de: {areaf}")

# Pide al usuario dos pares de números x1, y1, x2, y2, que representen dos números en el plano. Calcula y muestra la distancia entre ellos.
import math
def B():
    x1, y1, x2, y2 = map(int,input("Ingresa dos pares de numeros separados por espacio: ").split())
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"La distancia entre los numeros es de: {distancia}")

# Escribir  un  programa  que  lea  un entero  positivo  n,
# introducido  por  el  usuario  y después muestre en pantalla
# la suma de todos los enteros desde 1 hasta n. 
# La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = 𝑛(𝑛+1)2
def C():
    entero = int(input("Ingresa un N° entero positivo: "))
    if entero <= 0:
        print("No sea imbecil, le dije que ingrese un numero POSITIVO")
    else:
        for i in range(entero+1):
            suma = (i*(entero+1)/2)
        print(f"La suma de 1 hasta {entero} es de: {int(suma)}")

# Una  tienda ofrece  un  descuento  del 15%  sobre el  total  de  la  compra
# y  un  cliente desea saber cuánto deberá pagar finalmente por su compra.
def D():
    compra = int(input("Cual es el valor de su compra: "))
    descuento = compra * 0.15
    total = compra - descuento
    print(f"Tuviste un descuento del 15%, Total a pagar: {int(total)}")

# Elabore un  programa que  realice  la  conversión  de  cm.  a  pulgadas. 
# Donde  1  cm  = 0.39737  pulgadas.  Por  lo  tanto,  
# el  usuario proporcionaráel  dato  de  N  cm.  
# y  el programa dirá a cuantas pulgadas es equivalente.
def E():
    centimetros = float(input("Ingresa los centimetros: "))
    pulgadas = centimetros * 0.39737
    print(f"{int(centimetros)} centimetros, son {pulgadas:.2f} pulgadas")

def punto1():
    opcion = int(input("""
              [-------------------------------------]
              [           Menu Actividad 1          ]
              |-------------------------------------| 
              [Opcion 1. Area de un circulo         ]
              [Opcion 2. Distancia entre dos puntos ]
              [Opcion 3. Suma de enteros positivos  ]
              [Opcion 4. Descuento del 15%          ]
              [Opcion 5. Conversion de cm a pulgadas]
              [-------------------------------------]
              |Elige ua opcion: """))
    if opcion == 1:
        A()
    elif opcion == 2:
        B()
    elif opcion == 3:
        C()
    elif opcion == 4:
        D()
    elif opcion == 5:
        E()
    else:
        print("Elige una opcion valida")


# Actividad 2 ESTRUCTURAS CONDICIONALES

# Leer dos enteros A y B y calcular F de acuerdo con las siguientes reglas:
# a)F = 2 * A + B  Si  A^2–B^2 < 0
# b)F = A^2 –2 * B Si  A^2–B^2 = 0
# c)A + B          Si  A^2–B^2 > 0
def A2():
    a, b = map(int,input("Ingresa dos numeros enteros separados por espacio: ").split())
    if a**2 - b**2 < 0:
        f = 2 * a + b
        print(f"El calculo 1 de F es: {f}")
    elif a**2 - b**2 == 0:
        f = a**2 - 2 * b
        print(f"El calculo 2 de F es : {f}")
    elif a**2 - b**2 > 0:
        suma = a + b
        print(f"El calculo 3 de F es: {suma}")

#Un proveedor de estéreos ofrece un descuento del 10%
# sobre el precio sin IVA de algún aparato  si  este  cuesta  $2000  o  más.
# Además,  independiente  de  esto  ofrece  un  5%  de descuento  si  la  marca  es  NOSY.  Determinar  cuánto  pagaría  con  IVA  incluido  un  cliente cualquier por la compra de su aparato.
def B2():
    precio = float(input("Cual es el valor de su producto: "))
    marca = str(input("Cual es la marca de su producto: "))
    marca = marca.upper()
    if precio >= 2000 and marca != "NOSY":
        descuento1 = precio * 0.10
        total = precio - descuento1
        print(f"Obtuviste un descuento del 10%, Total a pagar: {total}")
    else:
        if precio < 2000 and marca == "NOSY":
            descuento2 = precio * 0.05
            total = precio - descuento2
            print(f"Obtuviste un descuento del 5%, Total a pagar: {total}")
        else:
            if precio >= 2000 and marca == "NOSY":
                descuento3 = precio * 0.15
                total = precio - descuento3
                print(f"Obtuviste un descuento del 15%, Total a pagar: {total}")
            else:
                print(f"No obtuvistes decuentos, Total a pagar: {precio}")
def punto2():
    opcion = int(input("""
              [-------------------------------------]
              [           Menu Actividad 2          ]
              |-------------------------------------| 
              [Opcion 1. Calculo de F               ]
              [Opcion 2. Descuento por valor y marca]
              [-------------------------------------]
              |Elije una opcion: """))
    if opcion == 1:
        A2()
    elif opcion == 2:
        B2()
    else:
        print("Elije una opcion valida.")


# Actividad 3 CICLOS REPETITVOS

# Escriba un algoritmo tal que dado como datos X números enteros, 
# obtenga el número de ceros  que  hay  entre  estos  números. 
# Por  ejemplo,  si  se  ingresa  6  datos:  9  0  4  8  0  1  El algoritmo arroja que hay 2 ceros.
def A3():
    c = 0
    numeros = int(input("Ingresa uno o mas numeros sin espacios: "))
    for i in str(numeros):
        if i == "0":
            c += 1
    print(f"Hay {c} ceros.")
    
# Ingresar por teclado 100 números enteros 
# y calcular cuántos de ellos son pares. Se imprime el resultado.
def B3():
    c = 0
    cien = int(input("Ingresa cien numeros sin espacios: "))
    for i in str(cien):
        if int(i) % 2 == 0:
            c += 1
    print(f"{c} numeros son pares")

#Actividad 3 VECTORES

# Cargar un vector de 100 posiciones con numero enteros, a partir de este crear 2 vectores;
# uno con los  números  pares  y  el  otro  con  los  numero  impares,  
# además  decir  de  los  vectores  cual  es  más grande  y el  número  de  elementos  en  cada vector.  
# Inicialmente  los  vectores  estarán  limpios, esto quiere decir que todas las posiciones tendrán el valor 0 (cero).


def vectores():
    vector = [41, 50, 75, 98, 45, 34, 62, 38, 18, 70, 22, 52, 82, 34, 6, 53, 33, 45, 21, 92, 83, 12, 45, 27, 56, 33, 49, 10, 95, 24, 90, 40, 58, 3, 65, 70, 3, 37, 30, 32, 86, 45, 47, 6, 27, 65, 55, 14, 51,10, 77, 24, 29, 56, 34, 65, 97, 28, 2, 61, 66, 90, 33, 80, 29, 72, 66, 87, 61, 77, 3, 90, 43, 70, 39, 52, 86, 40, 56, 55, 51, 40, 93, 73, 24, 23, 87, 85, 74, 86, 18, 62, 19, 45, 16, 89, 86, 6, 40, 87]
    listapar = []
    listaimpar = []
    for i in vector:
        if i % 2 == 0:
            listapar.append(i)
        if i % 2 !=0:
            listaimpar.append(i)
    if len(listapar) > len(listaimpar):
            print(f"""
                  El vector mas grande es:
                        {listapar}
                  """)
    else:
            print(f"El vector mas grande es {listaimpar}")
    print(f"La lista de pares tiene {len(listapar)} pares, y la lista de impares tiene {len(listaimpar)} impares.")
vectores()
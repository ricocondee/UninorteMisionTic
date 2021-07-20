#Obtener los primeros N numeros naturales positivos.

num = int(input("numero: "))
i = 1
suma = 0

while(i <= num):
    suma = suma + i
    i = i  + 1
print(f"suma: {suma}")

# Calcular independientemente de los numeros pares e impares entre 1 y N.
""" i = 1
sumapar = 0
sumaimpar = 0
num = int(input("Numero: "))

while(i <= num):
    if(i %2 == 0):
        sumapar += i
    else:
        sumaimpar += i
    i += 1
print(f"La suma de los pares es: {sumapar}")
print(f"La suma de los impares es: {sumaimpar}") """

#Muestre los numeros del 1 al N (ambos incluidos) divisibes entre 4 y 5.

""" i = 1
num = int(input("Numeros: "))
while(i <= num):
    if( i %4 == 0 and i % 5 == 0):
        print(f"{i}, es divisible por 4 y 5")
    else:
        if(i % 4 == 0):
            print(f"{i}, es divisible por 4")
        else:
            if (i % 5 == 0):
                print(f"{i}, es divisible por 5")
            else:
                print(f"{i}, no es divisible por 4 y 5")
    i = i + 1 """

#Escribir un algoritmo que imprima los 10 primeros números pares comenzando en 2
#e imprima también sus respectivos cubos.

""" i = 2
while (i <=20):
    if i % 2==0:#sin terminar
        print(i)
    i += 2 """

#Elabore un algoritmo que muestre los términos de la serie de Fibonacci que sean menores a 100

#Serie = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

""" num1 = 0
num2 = 1
suma = num1 + num2
print(num1)
print(num2)
while(suma < 10):
    print(suma)
    num1 = num2
    num1 = suma
    suma = num1 + num2 """
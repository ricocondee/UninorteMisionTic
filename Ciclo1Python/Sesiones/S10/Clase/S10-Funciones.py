# Las combinaciones o coeficientes
# binomiales son una serie de números
# que indican la cantidad de formas en
# que se pueden extraer subconjuntos
# a partir de un conjunto dado.
# Para calcular combinaciones se debe
# utilizar la siguiente fórmula: c=n!-m!*(n-m)!

#Funcion factorial
""" def factorial(num):
    f = 1
    for i in range(1,num+1):
        f=f*i
    return f

#Codigo principal
n = int(input("Tamaño del conjunto: "))
m = int(input("Tamaño del grupo a crear: "))
nf = factorial(n)
mf = factorial(m)
nmf = factorial(n-m)
c = nf/(mf*nmf)
print(f"La cantidad de combinaciones es {c}") """

#Escribamos una función numAleatorio() que retorne un número aleatorio entre 100 y 130, 
#excepto los números 110, 115 y 120.
#Adicionalmente, una función numeros que imprima diez números aleatorios 
#(retornados por la función numAleatorio()) alternando par, impar, comenzando por par.

""" import random
num2 = int(input("Inicio de rango: "))
num3 = int(input("final de rango: "))
def numaleatorio():
    num = 100
    continuar = True
    while continuar: #(TERMINAR)
        num = random.randint(num2,num3)
        if num!= 110 and num!= 115 and num != 120:
            break
    return num
def numeros():
    for i in range(10):
        print(numaleatorio())
numeros() """

#Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección 
#es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si 
#contiene el símbolo "@".

""" def arroba(email):
    simbolo = "@"
    correovalido = False
    for i in email:
        if i == simbolo:
            return True
    return False
correo = input("Tu email: ")
if arroba(correo):
    print("Direccion de correo valida")
else:
    print("Correo no valido revisa que tenga el '@'") """

#Escribir una función que, dado un número de DNI, retorne True si el número es válido y False 
#si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

numced = int(input("Ingresa tu DNI: "))
def cedula(dni):
    cantidad = 0
    while dni != 0:
        cantidad += 1
        dni = dni //10
    return cantidad == 7 or cantidad == 8 or cantidad == 10
if cedula(numced):
    print("es valida.")
else:
    print("No es valida.")
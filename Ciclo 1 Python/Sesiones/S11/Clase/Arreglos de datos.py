#Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y crear una función que rellene el array 
# o arreglo con los múltiplos de un número pedido por teclado. Por ejemplo, si defino un array de tamaño 5 y elijo un 3 
# en la función, el array contendrá 3, 6, 9, 12, 15. Muestralos por pantalla usando otra función distinta.

""" n = int(input("Tamaño del array: "))
m = int(input("Ingrese el multiplo: "))
multiplos = []
for i in range(1, n+1):
    multiplos.append(i*n)
print(f"El arreglo multiplos: {multiplos}") """

#Dado el siguiente arreglo de números:
#[1, 5, 8, 3, 30, 9, 13]
#Imprimir en pantalla programáticamente los números impares mayores a 3.

""" a =[1, 5, 8, 3, 30, 9, 13]
b =[]
for i in a:
    if i > 3 and i%2!=0:
        b.append(i) #append anexa un nuevo elemento del array unidimencional
print(f"El nuevo arreglo: {b}") """

#Crea dos arrays o arreglos unidimensionales que tengan el mismo tamaño (lo pedirá por teclado), 
# en uno de ellos almacenarás nombres de personas como cadenas, en el otro array o arreglo 
# ira almacenando la longitud de los nombres.

""" a = int(input("Ingrese el tamaño de los arreglos: "))
b =[]
c =[]
for i in range(0,a):
    b.append(input("Ingrese el nombre de la persona: "))
    c.append(len(b[i]))
print(b)
print(c) """

#Dada las siguientes notas almacenadas en un arreglo:
#[20, 15, 12, 11, 8, 4, 1]
#Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. 
#Luego programáticamente calcule el promedio de notas descontando la nota eliminada.

""" notas = [20, 15, 12, 11, 8, 4, 1]
maxi = 20
mini = maxi
for i in notas:
    if i < mini:
        mini = i
print(f"La nota mas baja es: {mini}")
notas.remove(mini)
print(notas)
suma = 0
for j in notas:
    suma = suma + j
print(suma)
print(suma/len(notas)) """

# Dado una lista de 10 posiciones, cree un algoritmo que lea y escriba cada uno de sus elementos.

""" def lista():
    x = 10
    lista =[]
    while x >0:
        y = int(input("Numero: "))
        lista.append(y)
        x -= 1
    return(lista)
print(lista()) """

# Dado una lista de N posiciones, calcular la suma de todos sus elementos.

def lista():
    x = 10
    lista = []
    while x > 0:
        y= int(input("Numero: "))
        lista.append(y)
        x -=1
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    print(suma)
    return(lista)
print(lista())

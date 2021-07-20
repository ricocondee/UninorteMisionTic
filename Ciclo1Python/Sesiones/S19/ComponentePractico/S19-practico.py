"""
Manejo de archivos

Continuemos ahora con otras opciones como escribir y actualizar un archivo desde Python.

Recordemos las opciones disponibles para el manejo de archivos.
Modo 	Descripción
'r' 	Abrir el archivo en modo lectura, este es el valor por defecto
'w' 	Abrir el archivo para escritura, eliminará cualquier archivo existente con el mismo nombre
'x' 	Crear el archivo, si existe uno con el mismo nombre sacará un error
'a' 	Abrir el archivo para escribir. Todo lo escrito se adicionará al final del archivo
'b' 	Abrir en modo binario
't' 	Abrir en modo texto, este es el valor por defecto
'+' 	Abrir para lectura y escritura

Empecemos creando un archivo de texto llamado minuevoarchivo.txt. 
"""
def ejemplo1():
    nuevoArchivo = open('minuevoarchivo.txt', mode='w', encoding='utf-8-sig' )
    nuevoArchivo.write("Escribiendo desde Python")

ejemplo1()

#Ahora vamos a crear un diccionario y a imprimir todos los valores y el valor almacenado con la clave 2
def ejemplo2():
    diccionario = { 1 : 'lunes', 2:'martes', 3:'miercoles', 4:'jueves', 5:'viernes', 6:'sabado', 7:'domingo'}

    print(diccionario)
    print(diccionario[2])

ejemplo2()

# Actividad 1
#
# Vamos a elaborar un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano usando un diccionario como lo definimos anteriormente. 
def romans():
    romanos = { 1 : 'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8: 'VIII' , 9: 'IX', 10: 'X'}
    print("Ingresa un numero para saber su equivalente en romano")
    numero = int(input("Numero: "))
    if numero > 10:
        print("Ingresa numeros unicamente del 1 al 10")
    else:
        print(romanos.get(numero))
#Actividad 2 
#Recordemos una de las actividades que hicimos en sesiones anteriores.
#
#Diseña un programa con las siguiente características:
#
#    Que tenga una función caja que 
#       a. Cree un archivo recibo.txt
#       b. Solicite al usuario nombre y precio de cada producto.
#       d. Una función adicional llamada guardaProducto(nombre, precio, archivo) que reciba el nombre y el precio de cada producto y los escriba en el archivo recibo.txt.
#       e. Que después de llamar a guardaProducto le pregunte al usuario si tiene o no más artículos a ingresar. Si no tiene, el programa debe detenerse.
#    Al final de tus funciones, puedes simplemente llamar a la función caja para probar

def save(name, price, archiv):
    archiv.writelines("Producto: "+name+"\n Precio: $"+str(price)+"\n")
    
def box():
    archiv = open("C:/Users/ricoc/Desktop/UninorteMisionTic/Ciclo 1 Python/Sesiones/S19/Componente Practico/facture.txt", mode="w", encoding="UTF-8")
    name = input("Nombre del producto: ")
    price = int(input("Precio del producto: "))
    save(name, price, archiv)

    while True:
        count = input("Desea ingresar mas productos? (Y/N): ")
        count = count.upper()
        if count == "Y":
            name = input("Nombre del producto: ")
            price = int(input("Precio del producto: "))
            save(name, price, archiv)
        else:
            break
box()

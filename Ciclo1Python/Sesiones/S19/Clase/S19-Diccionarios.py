#Ejemplo para escribir dentro de un archivo.
""" nuevoarchivo = open("C:/Users/ricoc/Desktop/UninorteMisionTic/Ciclo 1 Python/Sesiones/S19/Clase/miarchivo.txt", mode="w", encoding="UTF-8")
nuevoarchivo.write("Tú te ves asesina con ese mahón, me matas sin un pistolón.") """

#Ejemplo para crear un diccionario e imprimir todos los valores y el valor almacenado con la clave 2.
""" diccionario= {1:'Lunes', 2:'Martes', 3:'Miercles', 4:'Jueves', 5:'Viernes', 6:'Sabado', 7:'Domingo'}
print(diccionario)
print(diccionario[6]) """

#Actividad propuesta.
#Ejercicio 1:

#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono, y lo guarde
#en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en
#<direccion> y su número de teléfono es <teléfono>.

""" nombre = input("Nombre: ")
edad = int(input("Edad: "))
direccion = input("Direccion: ")
telefono = int(input("Telefono: "))
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su numero de telefono es {persona['telefono']}")
 """

#Ejercicio 2:

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
#{'Matemáticas':6,'Física':4,'Química':5} y después muestre por pantalla los créditos de cada asignatura
#en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas
#del curso, y <créditos> son sus créditos. AL final debe mostrar también el número total de créditos
#del curso.

""" curso ={'Matematicas': 6, 'Fisica':4, 'Quimica':5}
totalcreditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos,'creditos')
    totalcreditos += creditos
print("Total creditos del curso: ", totalcreditos)
 """


#Ejercicio 3:

#Ejercicio 3.
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
#usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
#Fruta    Precio
#------   -------- 
#Platano  1.35
#Manzana  0.80
#Pera     0.85
#Naranja  0.70

""" frutas = {'Platano':1.35, 'Manzana':0.80, 'Pera': 0.85, 'Narnja': 0.70}
fruta = input("Que fruta desea?: ").title()
kg = float(input("Cuantos kilos?: "))
if fruta in frutas:
    print(kg, 'kilos de,',fruta, 'tiene un costo de $: ',frutas[fruta]*kg)
else:
    print("Lo lamentamos, la fruta", fruta, "no se encuntra disponible")
     """
#Ejercicio propuesto utilizando el formato CSV(Valores separados por coma)
#El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
#Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), 
#Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
#Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

#Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.
#
#Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el 
#mínimo, el máximo y la media de dada columna.

def clean(cifra):
    cifra = cifra.replace('.', '')
    cifra = cifra.replace(',','.')
    return float(cifra)

def preprocessed(ruta):
    try:
        f = open(ruta, 'r')
    except FileNotFoundError:
        print("El archivo no existe")
        return
    lineas = f.readlines()
    f.close()
    claves = lineas[0]
    claves = claves[:-1].split(';')
    cotizaciones = {}
    for i in claves:
        cotizaciones[i] = []
    for linea in lineas[1:]:
        linea = linea[:-1].split(';')
        cotizaciones[claves[0]].append(linea[0])
    for j in range(1, len(cotizaciones)):
        cotizaciones[claves[j]].append(clean(linea[j]))
    return cotizaciones
def resumequotes(cotizaciones, ruta):
    del(cotizaciones['Nombre'])
    f = open(ruta,'w')
    f.write('Nombre')
    for clave in cotizaciones.keys():
        f.write(';'+ clave)
    f.write('\nMinimo')
    for valores in cotizaciones.values():
        f.write(';'+str(min(valores)))
    f.write('\nMaximo')
    for valores in cotizaciones.values():
        f.write(';'+str(max(valores)))
    f.write('\nPromedio')
    for valores in cotizaciones.values():
        f.write(';'+str(sum(valores)/len(valores)))
    f.close()
    return
cotizaciones = preprocessed("C:/Users/ricoc/Desktop/UninorteMisionTic/Ciclo 1 Python/Sesiones/S19/Clase/cotizacion.csv")
resumequotes(cotizaciones,"C:/Users/ricoc/Desktop/UninorteMisionTic/Ciclo 1 Python/Sesiones/S19/Clase/resumeQuotes.csv")
def archivospython():
    archivo = open("F:/UninorteMisionTic/Ciclo 1 Python/Sesiones/S18/Clase/miarchivo.txt", 'r')
    texto = archivo.read()
    print(texto)


def archivos2():
    archivo = open("F:/UninorteMisionTic/Ciclo 1 Python/Sesiones/S18/Clase/miarchivo.txt", 'r')
    linea = archivo.readline()
    print(linea)
    print("Lei la primera linea, vamos por la segunda")
    linea = archivo.readline()
    print(linea)


#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los 
#clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no 
#existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar 
#el teléfono de un cliente. El listín debe estar guardado en el fichero de texto `listin.txt` donde 
#el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta

def leertelefonos(arch, cliente):
    
    # Función que devuelve el teléfono de un cliente de un fichero dado.
    # Parámetros:
    #     arch: Es un fichero con los nombres y teléfonos de clientes.
    #     cliente: Es una cadena con el nombre del cliente.
    # Devuelve: 
    #     El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o
    #     el fichero no existe.
    
    try:
        f = open(arch,'r')
    except FileNotFoundError:
        return("El archivo "+ arch +" no existe!\n")
    else:
        directorio = f.readlines()
        f.close()
        directorio = dict([tuple(line.split(','))for line in directorio])
        if cliente in directorio:
            return directorio[cliente]
        else:
            return("El cliente"+ cliente +" no existe!\n")

def agregartelefono(arch,cliente,tel):
    
    # Función que añade el teléfono de un cliente de un fichero dado.
    # Parámetros: 
    #     arch: Es un fichero con los nombres y teléfonos de los clientes.
    #     cliente: Es una cadena con el nombre del cliente.
    #     tel: Es una cadena con el teléfono del cliente.
    # Devuelve:
    #     Un mensaje informando sobre si el teléfono se ha agregado o ha habido algún problema.
    
    try:
        f = open(arch,'a')
    except FileNotFoundError:
        return("El archivo "+ arch + "no existe!\n")
    else:
        f.write(cliente+","+tel+"\n")
        f.close()
        return("El telefono se ha añadido. \n")

def eliminartelefono(arch,cliente):
    
    # Función que elimina el teléfono de un cliente en un fichero dado.
    # Parámetros:
    #     arch: Es un fichero con los nombres y teléfonos de los clientes
    #     cliente: Es una cadena con el nombre del cliente.
    # Devuelve: 
    #     Un mensaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
    
    try:
        f = open(arch,'r')
    except FileNotFoundError:
        return("¡El fichero "+ arch +" no existe!\n")
    else:
        directorio = f.readlines()
        f.close()
        directorio = dict([tuple(line.split(',')) for line in directorio])
        if cliente in directorio:
            del directorio[cliente]
            f = open(arch,'w')
            for nombre,telefono in directorio.items():
                f.write(nombre+" , "+telefono)
            f.close()
            return("!El cliente se ha borrado!\n")
        else:
            return("¡El cliente"+ cliente +" no existe!\n")

def creardirectorio(arch):
    
    # Función que crea un fichero vacío para guardar un listado telefónico.
    # Parámetros: 
    #     arch: Es un fichero.
    # Devuelve:
    #     Un mensaje informando sobre si el fichero se ha creado correctamente o no.
    
    import os
    if os.path.isfile(arch):
        respuesta = input("El archivo "+ arch +" ya existe. ¿Desea vaciarlo (S/N)?")
        if respuesta == "N":
            return "No se ha creado el archivo porque ya existe.\n"
    f = open(arch,'w')
    f.close()
    return "Se ha creado el fichero.\n"

def menu():
    print("Gestión del listado telefónico")
    print("1 - Consultar un teléfono")
    print("2 - Añadir un teléfono")
    print("3 - Eliminar un teléfono")
    print("4 - Crear el listado")
    print("0 - Terminar el listado")
    op = input("Elija la opción deseada: ")
    return op

def directorio():
    arch = "C:/Users/ricoc/Desktop/UninorteMisionTic/Ciclo 1 Python/Sesiones/S18/Clase/listado.txt"
    while True:
        op = menu()
        if op == "1":
            nombre = input("Introduzca el nombre del cliente: ")
            print(leertelefonos(arch,nombre))
        elif op == "2":
            nombre = input("Introduzca el nombre del cliente: ")
            telefono = input("Introduzca el telefono del cliente: ")
            print(agregartelefono(arch,nombre,telefono))
        elif op == "3":
            nombre = input("Introduzca el nombre del cliente: ")
            print(eliminartelefono(arch,nombre))
        elif op == "4":
            print(creardirectorio(arch))
        else:
            break
    return

directorio()

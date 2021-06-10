""" def archivos_python():
    archivo = open("F:/UninorteMisionTic/Ciclo 1 Python/Sesiones/S18/Clase/miarchivo.txt", 'r')
    texto = archivo.read()
    print(texto)
archivos_python() """

def archivos2():
    archivo = open("F:/UninorteMisionTic/Ciclo 1 Python/Sesiones/S18/Clase/miarchivo.txt", 'r')
    linea = archivo.readline()
    print(linea)
    print("Lei la primera linea, vamos por la segunda")
    linea = archivo.readline()
    print(linea)
archivos2()

#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los 
#clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no 
#existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar 
#el teléfono de un cliente. El listín debe estar guardado en el fichero de texto `listin.txt` donde 
#el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta

def leertelefonos(arch, cliente,):
    
    # Fincion que devuelve el numero celular del cliente de un fichero dado
    # parametros:
    #   arch: es un fichero con los nombres y telefonos de clientes
    #   cliente: es una cadena con el nombre del cliente
    # devuelve:
    #   El telefono del cliente guardado en el fichero o un mensaje de error si el telefono o el fichero no existe.
    
    try:
        f = open(arch, 'r')
    except FileNotFoundError:
        return(f"El archivo {arch} no existe!\n")
    else:
        directorio = f.readlines()
        f.close()
        directorio = dict([tuple(line.split(','))for line in directorio])
        if cliente in directorio:
            return directorio[cliente]
        else:
            return(f"El cliente {cliente} no existe!\n")
        
def eliminartelefono(arch, cliente):
    
    # Funcion que elimina el telefono de un cliente en un fichero dado
    # Parametros:
    #     arch: Es un fichero con los nombres del cliente.
    #     cliente: Es una cadena con el nombre del cliente.
    # Deviuelve:
    #     Un mensaje informando sobre si el telefono se ha borrado o ha habido un problema.
    
    

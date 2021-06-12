#Solucion parte 1 Lactocatibe

matriz = []
matriz2 = []
def asignacion():
    filas = 5
    columnas = 4
    print("Ingrese los datos en el mismo orden y separados por espacio.")
    for j in range(filas):
            punto, ide, litros1, tiempo1, = map(int,(input(f"Camión {j+1}, N° Punto, ID del camion, Litros asignados, Tiempo asignado:  ").split()))
            matriz.append([punto, ide, litros1, tiempo1])
    print()
    for f in matriz:
        print("[", end=" ")
        for e in f:
            print("{:8.2f}".format(e), end=" ")
        print("]")
    print()
    menu()
def reparto():
        filas = 5
        columnas = 4
        print("Ingrese los datos en el mismo orden y separados por espacio.")
        for j in range(filas):
            punto, ide, litros2, tiempo2, = map(int,(input(f"Camión {j+1}, N° Punto, ID del camion, Litros despachados, Tiempo de entrega registrado:  ").split()))
            matriz2.append([punto, ide, litros2, tiempo2])
        print()
        for f in matriz2:
            print("[", end=" ")
            for e in f:
                print("{:8.2f}".format(e), end=" ")
            print("]")
        print()
        menu()
def calculo():
    nuevo = matriz2[2][1] / matriz[2][1] *100
    print(nuevo)
def menu():
            opcion = int(input("""
                                    [----------Menu de opciones----------]
                                    [------------------------------------]
                                    [1. Registrar datos antes de reparto ]
                                    [------------------------------------]
                                    [2. Registrar datos depues de reparto]
                                    [------------------------------------]
                                    [3. Resultados de eficiencia         ]
                                    [------------------------------------]
                                    [4. Salir                            ]
                                    [------------------------------------]
                                    |Elije una opcion: """))
            if opcion == 1:
                asignacion()
            if opcion == 2:
                reparto()
            if opcion == 3:
                calculo()
            else:
                print("Gracias por usar nuestro software.")
menu()
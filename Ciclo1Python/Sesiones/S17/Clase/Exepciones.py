def suma(a,b):
    x = a + b
    print("Resultado: ", x)

def resta(a,b):
    x = a - b
    print("Resultado: ", x)
    
def multiplicacion(a, b):
    x = a * b
    print("Resultado: ", x)
def division(a, b):
    x = a/b
    print("Resultado: ", x)
    
while True:
    try:
        a = int(input("Numero 1: "))
        b = int(input("Numero 2: "))
        op = str(input("""
                          [  Menu principal ]
                          [1. Suma          ]
                          [2. Resta         ]
                          [3. Multiplicacion]
                          [4. Division      ]
                          [Elije una opcion: """))
        if op == '1':
            suma(a,b)
            break
        elif op == '2':
            resta(a, b)
            break
        elif op == '3':
            multiplicacion(a, b)
            break
        elif op == '4':
            division(a, b)
            break
        else:
            print("Opcion invalida, intente de nuevo")
    except ZeroDivisionError:
        print("No es posible hacer esta division.")
    except:
        print("Error")
        op = '?' 
    
def ej2():
    try:
        num = 10
        string = "Hola a todos"
        print(num + string)
        print(num / 2)
    except ZeroDivisionError:
        print("Division no valida entre enteros y cadenas ")
    except (ValueError,TypeError):
        print("Ha ocurrido un error.")
        
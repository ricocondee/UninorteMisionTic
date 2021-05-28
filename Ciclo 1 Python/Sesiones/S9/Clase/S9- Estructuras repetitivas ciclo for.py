""" num = int(input("Cantidad de estudiantes: "))
suma = 0

for c in range(num):
    nota = float(input(f"Nota {c+1}: "))
    suma = suma + nota

prom = suma / num
print(f"El promedio es: {prom}")
 """
#Leer N números e imprimir cuántos son positivos, negativos y neutros
""" 
cpos = 0
cneg = 0
cneu = 0

n = int(input("Cantidad de numeros: "))
for i in range(0,n):
    num = int(input("Numeros: "))
    if num == 0:
        cneu+=1
    else:
        if num > 0:
            cpos+=1
        else:
            cneg+=1
print(f"La cantidad de positivos es: {cpos}")
print(f"La cantidad de negativos es: {cneg}")
print(f"La cantidad de neutros es: {cneu}") """

#Elaborar un algoritmo que permita mostrar el sueldo promedio de un grupo de empleados

""" emple = int(input("Cantidad de empleados: "))
i=0
for p in range(emple):
    suminimo = float(input(f"Ingrese su sueldo {p+1}: "))
    i = i+suminimo

promedio = i/emple
print(f"El sueldo promedio es: {promedio}") """

#Dado un rango de números enteros, obtener la cantidad de números pares que contiene.

""" i = int(input("Ingrese los numeros: "))
f = int(input("Ingrese los numeros: "))
p=0
for c in range(i,f+1):
    if c % 2 ==0:
        p+=1 #sin terminar
        print(p) """

#EJERCICIOS PROPUESTOS
#1. Crear un algoritmo para hallar el factorial de un número, el factorial es el producto de todos
#los números consecutivos desde la unidad hasta el número, por ejemplo 3! es 1 x 2 x 3 = 6
""" num = int(input("Ingrese un numero: "))
fact = 1
for f in range(2, num+1):
    fact = fact * f
print(f"{num}! (factorial) es de: {fact}") """
# 2. Determine cuantos numeros primos hay en los primeros N núneros enteros positivos.
 
""" num = int(input("Ingrese un numero: "))
c1 =0
c2 =0
if num <= 0:
    print("Deben ser numeros enteros positivos.")
else:
    for pri in range(1,num):
        c1 = 0
        for pri2 in range(1,pri):
            if pri%pri2==0:
                c1+=1
        if c1 < 2:
            print(pri)
            c2+=1
    print(f"Hay {c2} primos") """



# 3. Serie de Fibonacci (For)

""" num = int(input("Numero: "))
def fibo(s):
    a=0
    b=1
    for f in range(s):
        c = a+b
        a = b
        b = c
    return b
for t in range(num):
    print(fibo(t)) """
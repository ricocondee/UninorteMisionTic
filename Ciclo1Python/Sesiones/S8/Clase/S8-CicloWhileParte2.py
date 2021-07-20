# Ahora vamos a elaborar un algoritmo que pida un numero al usuario, 
# e imprima todos los numeros pares desde 2 hasta el numero pero que termine el proceso si llega al 10

""" num = int(input("Ingresa un numero"))
i = 2
while i < num:
    print(i)
    if (i == 10):
        break
    i+= 2 """
# (La sentencia break nos permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle.
# Esto significa que una vez se encuentra la palabra break, el bucle se habrá terminado.)


# Escribe el código un ciclo para obtener el número de digitos de un número ingresado
# por el usuario pero saltarse si el digito es 4

""" num = int(input("Ingrese un numero: "))
digitos = 0
while (num > 0):
    if num % 10 == 4:
        num=num//10
        continue 
    digitos = digitos + 1
    num = num //10
    print(digitos)
 """
#(El uso de continue al igual que el ya visto break, nos permite modificar el comportamiento de de los bucles while y for.

# Concretamente, continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.

# A diferencia del break, el continue no rompe el bucle sino que finaliza la iteración actual, haciendo que todo el código que va después se salte, y se vuelva al principio a evaluar la condición.)


#Dado el valor de E^x se puede calcular por aproximación de la siguiente suma:
# E = 1 + x + x^2/2! + x^3/3! + .... + x^n/n!
#Realizar el algoritmo que tome un valor para X y calcule E^x hasta que x^n/n!
#(error o aproximación) sea menor a 0.00001

""" x = int(input("Ingrese el valor de X: "))

e = 1
num = 1
den = 1
i = 1

num = x ** i
den = den * i
i=i+1
e = e + num/den
while not(num/den < 0.00001):
    num = x**i
    den = den * 1

    e = e + num/den
print("\nSALIDA")
print("-------------------")
print("e elevado al ",x," es: ",e) """
 
#Crear un algoritmo que indique si un numero es cubo perfecto(armstrong) o no, se dice que un numero es
#cubo perfecto si al sumar los cubos de sus digitos dan el mismo numero, 
# por ejemplo 153, cubos de sus digitos
#1^3 + 5^3 + 3^3 = 153 el numero 153 es cubo perfecto.
""" 
s=0
num = int(input("Inrese un numero: "))
t = num
while (t>0):
    d = t % 10
    t=t//10
    s = (int) (s + d**3)

if (num == s):
    res = "CUBO PERFECTO "
else:
    res = "EL CUBO NO ES PERFECTO"
print(f"el resultado es: {res}") """

#Dado un numero, Determine si es un numero primo. (recuerde que un numero primo es aquel que solo es divisible por 1 y por si mismo).
""" num = int(input("Ingrese un numero:"))
sw = True
i=2
while(i<=num/2):
    if (num%i==0):
        sw = False
        break
    i=i+1

if(sw):
    res= "ES PRIMO"
else:
    res= "NO ES PRIMO"
print(res) """

#Tablas de multiplicar usando While.
""" 
num = int(input("Numero: "))
limite = 10
i =1
while i<=limite:
    res = num*i
    print(num, " X ",i, " = ",res)
    i=i+1 """
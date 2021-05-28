""" #Escriba un programa que pida tres numeros y que imprima sin son iguales, hay dos iguales o son diferentes
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
num3 = int(input("Ingresa un numero: "))
if num1 == num2 and num1 == num3:
    print("Los tres numeros son iguales.")
else:
    if num1 != num2 and num1 != num3:
        print("Los numeros son diferentes.")
    else:
        if num1 == num2 and num1 != num3:
            print("Dos nueros son iguales.")
        else:
            if num1 == num3 and num1 != num2:
                print("Dos nueros son iguales.")
            else:
                print("Ingresa datos validos.") """

#Escriba un programa que pida un año y que escriba si es bisiesto o no.
#Se recuerda que los años bisiestos son multiplos de 4, pero los multiplos de 100 no o son aunque los multiplos de 400 si.
""" 
year = int(input("Ingresa un año: "))
if year %4 == 0:
    print(f"{year} es bisiesto.")
elif year %400 == 0:
    print(f"{year} es bisiesto")
else:
    print(f"{year} no es bisiesto") """

#                                           MARATON PRACTICA 13 EJERCICIOS

#EJERCICIO 1
#En un almacén se descuenta el 20% del valor a pagar, si el total de la compra excede $200.000.
#Dado el valor que un cliente compró, determine el valor que debe pagar.
#Calcular e imprimir el valor que un cliente debe pagar por su compra

#EJEMPLOS
 #valor_compra=200000, valor_pagar=200000
 #valor_compra=300000, valor_pagar=240000
 #valor_compra=50000, valor_pagar=50000

""" valor1 = float(input("Ingrese el valor de su compra (sin puntos): "))
descuento = valor1*0.20
pagar = valor1 - descuento
if valor1 > 200000:
    print(f"Tu descuento es de ${descuento}, debes pagar ${pagar}")
else:
    print("Tu compra debe ser mayor a $200000 para recibir un descuento") """

#EJERCICIO 2
#Se requiere determinar, suministrado un mes (número de mes), cuantos días tiene ese mes.

#--------------------------
#| Mes            | Dia   |
#--------------------------
#|1,3,5,7,8,10,12 | 31    |
#--------------------------
#|4,6,9,11        | 30    |
#--------------------------
#|2               | 28/29 |
#--------------------------

#Indicar la cantidad de días del mes especificado
#EJEMPLOS
#mes = 1, Salida = 31
#mes = 2, Salida = 28
#mes = 15, Salida = Mes no valido
#mes = enero, Salida = Mes no valido

""" mes = int(input("Ingresa un mes en numeros: "))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print(f"El mes {mes} tiene 31 dias")
else:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print(f"El mes {mes} tiene 30 dias")
    else:
        if mes == 2:
            print(f"El mes {mes} puede tener 28 dias o 29 si el año es bisiesto" )
        else:
            print("mes no valido") """
#EJERCICIO 3
#En una frutera, se ofrece un descuento por volumen a la compra del kilo de manzanas, de acuerdo a la siguiente tabla.

#------------------------------------
#|cantidad comprada | % de descuento|
#------------------------------------
#|[0.00 - 2.00)     | 0.00          |
#------------------------------------
#|[2.00 - 5.00)     | 10.00         |
#------------------------------------
#|[5.00 - 10.00)    | 15.00         |
#------------------------------------
#|10.00+            | 20.00         |
#------------------------------------

#Dado el precio por kilo y la cantidad de kilos comprados, determine cuánto pagará un cliente por su compra.
#Determinar el valor a pagar por un cliente en una compra.
""" cantidad = int(input("Ingresa cuantos kilos de manzana compro. "))
preciokg = float(input("Ingresa cual es el valor por kilo. "))
preciof = preciokg * cantidad
if cantidad < 2.00:
    pago = preciokg * cantidad
    print(f"No tienes descuento, debes comprar mas de 2kg para tener uno, el valor de tu compra es de {pago}")
else:
    if cantidad >= 2.00 and cantidad < 5.00:
        descuento = preciof * 0.10
        pago = preciof - descuento
        print(f"Tu descuento es de 10%, el valor de tu compra es {pago}")
    else:
        if cantidad >= 5.00 and cantidad < 10.00:
            descuento = preciof * 0.15
            pago = preciof - descuento
            print(f"Tu descuento es de 15%, el valor de tu compra es {pago}")
        else:
            if cantidad >= 10.00:
                descuento = preciof * 0.20
                pago = preciof - descuento
                print(f"Tu descuento es de 20%, el valor de tu compra es {pago}")
            else:
                print("Error intenta nuevamente.") """ 

#EJERCICIO 4
#Durante una campaña de PyP, cierta EPS desea informar a sus afiliados sobre el riesgo de obesidad;
#para lo cual utiliza la siguiente tabla suministrada por la OMS.
#Dadas la estatura y el peso de una persona, determinar su nivel de riesgo

#-------------------------------------------------
#|Clasificación      | IMC (Kg/m^2)  | Riesgo    |
#-------------------------------------------------
#|Normal             | [18.5 - 24.9] | Promedio  |
#-------------------------------------------------
#|Sobrepeso          | [25.0 - 29.9] | Aumentado |
#-------------------------------------------------
#|Obesidad grado I   | [30.0 - 34.9] | Moderado  | 
#-------------------------------------------------
#|Obesidad grado II  | [35.0 - 39.9] | Severo    |
#-------------------------------------------------
#|Obesidad grado III | 40+           | Muy severo|
#-------------------------------------------------

#Informar el nivel de riesgo a una persona
#Nota : Todos los resultados se redondearán a un dígito decimal
#IMC = 14.356789 ==> 14.4
#IMC = 25.1389 ==> 25.1

""" peso = float(input("Ingrese su peso (KG): "))
estatura = float(input("Ingrese su estatura (Metros): "))
imc = peso/(estatura**2)
if imc >= 18.5 and imc <= 24.9:
    clasif = "Normal"
    riesgo = "Promedio"
    print(f"|Estado: {clasif} | Imc: {round(imc,1)} | Riesgo: {riesgo}| ")
else:
    if imc >= 25.0 and imc <= 29.9:
        clasif = "Sobrepeso"
        riesgo = "Aumentado"
        print(f"|Estado: {clasif} | Imc: {round(imc,1)} | Riesgo: {riesgo}| ")
    else:
        if imc >= 30.0 and imc <= 34.9:
            clasif = "Obesidad Grado 1"
            riesgo = "Moderado"
            print(f"|Estado: {clasif} | Imc: {round(imc,1)} | Riesgo: {riesgo}| ")
        else:
            if imc >= 35.0 and imc <= 39.9:
                clasif = "Obesidad Grado 2"
                riesgo = "Severo"
                print(f"|Estado: {clasif} | Imc: {round(imc,1)} | Riesgo: {riesgo}| ")
            else:
                if imc >= 40.0:
                    clasif = "Obesidad Grado 3"
                    riesgo = "Muy Severo"
                    print(f"|Estado: {clasif} | Imc: {round(imc,1)} | Riesgo: {riesgo}| ")
                else:
                 print("Debes ingresar el peso en Kg y la altura en Metros: ejemplo peso: 100 altura: 1.80") """

#EJERCICIO 5.
#Una compañía de alquiler de automóviles cobra un valor fijo de $300.000, por los primeros 3000Km
#de recorrido; La siguiente tabla indica los cobros adicionales que la compañía aplica a sus clientes

#------------------------------------------------
# |Km recorrido | Valor fijo | Adicional ($/Km) |
#------------------------------------------------
# |<=3000       | 300000     | 0                |
#------------------------------------------------
# |3000-10000   | 0          | 150              |
#------------------------------------------------
# |>10000       | 0          | 200              |
#------------------------------------------------

#Calcular el total a pagar
#EJEMPLOS
#ki = 100, kf = 500 ==> kr = 400, apagar = $300000
#ki = 100, kf = 4300 ==> kr = 4200, apagar = $300000 + (4200-3000)*150 = 480000
#ki = 1000, kf = 12000 ==> kr = 11000, apagar = 300000+(11000-10000)*200+(10000-3000)*150

""" kini = int(input("Ingresa los kilometros iniciles que tenia el vehiculo: "))
kfin = int(input("Ingresa los kilometros finales: "))
krec = kfin - kini
vfijo = 300000
kfijo1 = 3000
kfijo2 = 10000
if krec <= 3000:
    print(f"El valor a pagar es: ${vfijo}")
else:
    if krec > 3000 and krec <= 10000:
        vfinal = vfijo + (krec - kfijo1)*150
        print(f"Valor a pagar es: ${vfinal}")
    else:
        if krec > 10000:
            vfinal = vfijo +((krec - kfijo2)*200) + ((kfijo2 - kfijo1) *150)
            print(f"El valor a pagar es: ${vfinal}")
        else:
            print("Error intentalo de nuevo") """

#Ejercicio 6.
#Una tienda descuenta el 20%, si el valor total de la compra excede 1000000; proponga un programa
#que indique el valor a pagar por un cliente, conocido el valor de la compra.
#Calcular e indicar el valor a pagar
#EJEMPLOS
 #valor_compra = 500000, apagar = 500000
 #valor_compra = 1000000, apagar = 1000000
 #valor_compra = 1500000, apagar = 1200000
 #valor_compra = -500, apagar = "ERROR: datos invalidos"

""" compra = float(input("Ingrese el valor de su compra (sin puntos): "))
descuento = compra*0.20
valorf = compra - descuento
if compra > 1000000:
    print(f"Tu descuento es de ${descuento}, debes pagar ${valorf}")
else:
    print("Tu compra debe ser de mas de $1000000 para recibir un descuento. Total a pagar: ", compra) """

#EJERCICIO 7
#Se dispone de un termómetro para medir con exactitud la temperatura en un determinado lugar.
#Sin embargo, les basta con saber de manera aproximada si la temperatura se ajusta a los rangos siguientes:

#-------------------------------------------------
#|RANGO DE TEMPERATURA (°C) | SENSACIÓN TÉRMICA  |
#-------------------------------------------------
#|[-10 - 10)                | Mucho frio         |
#-------------------------------------------------
#|[10 - 15)                 | Poco frío          |
#-------------------------------------------------
#|[15 - 25)                 | Temperatura normal |
#-------------------------------------------------
#|[25 - 30)                 | Poco calor         |
#-------------------------------------------------
#|[30 - 45)                 | Mucho calor        |
#-------------------------------------------------
 
# Lea el valor temperatura y devuelva la sensación térmica correspondiente.

#               EJEMPLOS
#--------------------------------------
# |ENTRADA ESPERADA | SALIDA ESPERADA |
#--------------------------------------
# |28               | Poco calor      |
#--------------------------------------
# |-9               | Mucho frio      |
#--------------------------------------
# |53               | Fuera de rango  |
#--------------------------------------

""" temp = int(input("Ingresa la temperatura: "))
if temp >= -10 and temp < 10:
    sen = "Mucho frio"
    print(sen)
else:
    if temp >= 10 and temp < 15:
        sen = "Poco frio"
        print(sen)
    else:
        if temp >= 15 and temp < 25:
            sen = "Temperatura normal"
            print(sen)
        else:
            if temp >= 25 and temp < 30:
                sen = "Poco calor"
                print(sen)
            else:
                if temp >= 30 and temp <= 45:
                    sen = "Mucho calor"
                    print(sen)
                else:
                    print("Fuera de rango") """

# EJERCICIO 8.
# Se desea diseñar un algoritmo que escriba los nombres de los días de la semana en función del valor
# de una variable DIA introducida por teclado.
# Los días de la semana son 7; por consiguiente, el rango de valores de DIA será 1..7.
# Indicar el nombre del día de la semana
# EJEMPLOS
# 1 Lunes, 2 Martes, 8 Error

""" print("Para saber que dia es, indica el numero de dias que van en esta semana.")
dia = int(input("Introduce el dia en numero: "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Mieroles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
   print("Error") """

#EJERCICIO 9
#Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades, si la decisión se toma
#con base a la antigüedad en la empresa.
#               DATOS                                      EJEMPLO
# -----------------------------------              ----------------------------
# |Antigüedad (Años) | % reconocido |              |5      | 1000000 | 150000 |
# -----------------------------------              ---------------------------- 
# |<1 año            |            5%|              |10     | 3000000 | 450000 |
# -----------------------------------              ----------------------------
# |[1 y 2)           |            7%|
# -----------------------------------
# |[2 y 5)           |           10%|
# -----------------------------------
# |[5 y 10]          |           15%|
# -----------------------------------
# |>10               |           25%|
# -----------------------------------

#Calcular el valor que un empleado recibe como reparto de utilidades.

""" utilidad = float(input("Ingresa tu antiguedad en la enpresa (Años, ejemplo 0.5, 1, 1.5 etc): "))
salario = float(input("Ingresa tu salario: "))
if utilidad < 1:
    recono = salario*0.05
    print(f"Por tu labor te reconocemos el valor de ${recono}")
else:
    if utilidad >= 1 and utilidad < 2:
        recono = salario*0.07
        print(f"Por tu labor te reconocemos el valor de ${recono}")
    else:
        if utilidad >= 2 and utilidad < 5:
            recono = salario*0.10
            print(f"Por tu labor te reconocemos el valor de ${recono}")
        else:
            if utilidad >= 5 and utilidad <= 10:
                recono = salario*0.15
                print(f"Por tu labor te reconocemos el valor de ${recono}")
            else:
                if utilidad > 10:
                    recono = salario*0.25
                    print(f"Por tu labor te reconocemos el valor de ${recono}")
                else:
                    print("Error ingresa los datos nuevamente") """
    

#EJERCICIO 10
#Una empresa de bienes raíces ofrece programas de vivienda de interés social, bajo las siguientes condiciones:

#• Si los ingresos del comprador son inferiores a 1.5millones, la cuota inicial será del 15% del valor de la vivienda 
#  y el restante se dividirá en cuotas (iguales) mensuales durante diez (10)años.

#• Si los ingresos del comprador son mayores o iguales a 1.5m, la cuota inicial será del 30% del valor de la vivienda 
#  y el resto se distribuirá en pagos mensuales (iguales) en 7 años.

#Determinar el plan de pago del comprador.

""" ingmes = float(input("Introduce tu ingreso mensual (Millones, ejemplo 1.8): "))
valorviv = float(input("Introduce el valor de la vivienda: "))
cuotaini1 = 0.15
cuotaini2 = 0.30
if ingmes < 1.5:
    cuotaini3 = valorviv * cuotaini1
    pyears = (valorviv - cuotaini3) / (12*10)
    total = (pyears*120)
    print(f"La cuota inicial es de ${cuotaini3} y las cuotas mensuales son de ${round(pyears,0)}, durante 10 años debes pagar ${total} ")
elif ingmes >= 1.5:
        cuotaini3 = valorviv * cuotaini2
        pyears = (valorviv - cuotaini3) / (12*7)
        total = (pyears*84)
        print(f"La cuota inicial es de ${cuotaini3} y las cuotas mensuales son de ${round(pyears,0)}, durante 10 años debes pagar ${total} ") 
else:
    print("Ingresa datos validos.") """

#EJERCICIO 10
# Un supermercado ha colocado en oferta la venta al por mayor de cierto producto, ofreciendo un
# descuento del 15% por la compra de más de tres (3) docenas y 10% en caso contrario. Además por
# la compra de más de tres (3) docenas se obsequia una unidad del producto por cada docena en
# exceso (sobre las tres(3) inicialmente mencionadas).
# Diseñe un programa que determine el monto de la compra, el monto del descuento, las cortesías
# (unidades obsequiadas) y el valor a pagar por un cliente.

#                       DATOS
# ---------------------------------------------------------
# |com    | pun       | Salida esperada                   |
# ---------------------------------------------------------
# | 4     | 5000      | 20000, 3000, 1, 17000             |
# ---------------------------------------------------------
# | 2     | 500000    | 100000, 10000,  0, 90000          |
# ---------------------------------------------------------

# Determina el monto de la compra, el monto del descuento, las cortesías (unidades obsequiadas) y
# el valor a pagar por un cliente.

docena = int(input("Ingresa cuantas docenas compraste: "))
compra = int(input("Ingresa el valor de la docena: "))
nombre = input("Ingresa el nombre del producto: ")
pxu = compra*docena
if docena <= 3:
    desc = 0.10
    montod = pxu * desc
    valor = pxu - montod
    print(f"valor de la compra ${pxu} \nvalor del descuento ${montod} \n(Para obtener un regalo debes comprar mas de 3 docenas) \nValor total a pagar ${valor}")
else:
    if docena > 3:
        desc = 0.15
        montod = pxu * desc
        valor = pxu - montod
        win = (docena-3)*1
        print(f"valor de la compra: ${pxu} \nvalor del descuento: ${montod} \nfelcidades ganaste {win} {nombre}s mas \nValor total a pagar: ${valor}")
    else:
        print("Error")
""" dia = int(input("Ingrese el dia 1 a 7: "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")   
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Error, intente de nuevo") """

# Temperatura
""" temp = float(input("Temperatura (celcius): "))
if temp < 10:
    print("Hace mucho frio")
else:
    if temp < 15:
        print("Hace poco frio")
    else:
        if temp < 25:
            print("Temperatura normal")
        else:
            if temp < 30:
                print("Hace poco calor")
            else:
                print("Hace mucho calor") """

#Diseñe un algoritmo que lea un número entero de 3 cifras, y forme el mayor número posible con las cifras del número ingresado. El número formado debe tener el mismo signo que el número ingresado.
""" 
num1 = int(input("Numero"))
if num1 >= 100 and num1 <= 999 or num1 >= -999 and num1 <= -100:
    numaux = num1
    if num1 < 0:
        num1 = -num1
    cen = numaux // 100
    dec = num1%100//10
    uni = num1%100%10

    menor = cen 
    if dec < menor:
        menor = dec
    if uni < menor:
        menor = uni

    mayor = cen 
    if dec > mayor:
        mayor = dec
    if uni > mayor:
        mayor = uni

    medio = (cen + dec + uni) - (mayor + menor)
    if numaux > 0:
        num2 = (mayor * 100) + (medio * 10) + menor
    else:
        num2 = -1*(mayor * 100) + (medio * 10) + menor
    print(num2)
else:
    print("el numero no tiene cifras") """

#Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si éste se le asigna como un porcentaje de su salario mensual, que depende de su antigüedad en la empresa, de acuerdo con lo siguiente: 
#							Tiempo		     	   Utilidad
#			Menos de 1 año		 		        5% del salario
#			1 año o más y menos de 2 años		7% del salario
#			2 años o más y menos de 5 años		10% del salario
#			5 años o más y menos de 10 años		15% del salario
#			10 años o más				        20% del salario

""" salario = float(input("salario de la persona"))
antig = int(input("Antiguedad (meses)"))
if antig < 12:
    utilidad = salario * 0.05
elif antig >= 12 and antig < 24:
    utilidad = salario * 0.07
elif antig >= 24 and antig < 60:
    utilidad = salario * 0.1
elif antig >= 60 and antig < 120:
    utilidad = salario * 0.15
else:
    utilidad = salario * 0.2
print("Las utilidades fueron de $: ",round(utilidad,2)) """
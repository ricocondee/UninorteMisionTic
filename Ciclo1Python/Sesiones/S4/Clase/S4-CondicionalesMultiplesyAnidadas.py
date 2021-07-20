#          Multiples

edad = int(input("Edad: "))
if edad <0:
    print("La edad que usted digita es un numero negativo")
elif edad < 18:
    print("Eres menor de edad. ")
else:
    print("Eres mayor de edad. ")


#           Anidados

print("Este programa mezcla colores.")
print(" r. rojo  -  a. azul")
primera = input("Elije un color. [r o a]:")
if primera == "r" or primera == "R":
    print("a.Azul  -  v.Verde")
    segunda = input("Elije otro color. [a o v]:")
    if segunda =="a" or segunda == "A":
        print("El color es magenta.")
    else:
        print("El color es amarillo.")
else:
    print(" v.Verde  -  r.Rojo")
    segunda = input("Elije otro color [v o r]:")
    if segunda == "v" or segunda == "V":
        print("El color es cian.")
    else:
        print("El color es magenta.")
print("hasta la proxima")
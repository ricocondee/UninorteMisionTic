#Reto 2 Uninorte, Mision tic 2022
#Realizado por Emanuel Rico Conde @ricocondee
#ID de estudiante: 200171465

tipo1 = int(input()) #Medicamentos tipo 1
tipo2 = int(input()) #Medicamentos tipo 2

p=0 #Contador pacientes
t1=0 #Contador pacientes con medicamentos tipo 1
t2=0 #Contador pacientes con medicamentos tipo 2

if tipo1<=0 or tipo2<=0: #Condicion en caso de ser erreonea la categoria
    print(p)
    print(t1,"0.00%")
    print(t2,"0.00%")
else: #En caso de no serlo

    while True: #Indica que siempre sera verdadera la condicion
                                     #Codigo del reto 1
            presion1 = int(input())
            presion2 = int(input())
            if presion1 < 72 and presion2 < 65:
                t2+=1 
                tipo2=tipo2-4
            elif presion1 >= 72 and presion1 < 107 and presion2 >=65 and presion2 <= 73:
                tipo1=tipo1-0
            elif presion1 >= 107 and presion1 < 124 and presion2 >= 73 and presion2 <= 81:
                tipo1=tipo1-0
            elif presion1 >= 124 and presion1 < 138 and presion2 >= 81 and presion2 <= 93:
                t1+=1
                tipo1=tipo1-2
            elif presion1 >= 138 and presion1 < 156 and presion2 >= 93 and presion2 <= 102:
                t1+=1
                tipo1=tipo1-4
            elif presion1 >= 156 and presion1 < 175 and presion2 >= 102 and presion2 <= 114:
                t1+=1
                tipo1=tipo1-8
            elif presion1 >= 175  and presion2 >= 114:
                t1+=1
                tipo1=tipo1-16
            elif presion1 >= 136  and presion2 < 92:
                t1+=1
                tipo1=tipo1-12
            p+=1
            if tipo1 <=0 or tipo2<=0: #Condicion para que me vuelva a pedir la presion
                break #Romper el ciclo en caso de que la condcion de arriba se cumpla
    print(p)
    porc1= t1/p*100  #Formula para el porcentaje de pacientes atendidos con el medicamento tipo 1 respecto al total
    porc2 = t2/p*100 #Formula para el  porcentaje de pacientes atendidos con el medicamento tipo 2 respecto al total
    print(f"{t1} {porc1:.2f}%") 
                                #f"{var:.2f}" Redondea los decimales a dos cifras
    print(f"{t2} {porc2:.2f}%")
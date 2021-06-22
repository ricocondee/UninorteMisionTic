#Reto 1 Uninorte, Mision tic 2022
#Realizado por Emanuel Rico Conde @ricocondee
#ID de estudiante: 200171465

presion1 = int(input("Ingrese su presion Sistolica: "))
presion2 = int(input("Ingrese su presion Diastolica: "))
if presion1 < 72 and presion2 < 65:
    print(chr(27)+'\033[93m'+"Hipotension Alerta Amarilla.")
elif presion1 >= 72 and presion1 < 107 and presion2 >=65 and presion2 <= 73:
    print(chr(27)+'\033[32m'+"Optima Alerta Verde.")
elif presion1 >= 107 and presion1 < 124 and presion2 >= 73 and presion2 <= 81:
    print(chr(27)+'\033[32m'+"Normal Alerta Verde.")
elif presion1 >= 124 and presion1 < 138 and presion2 >= 81 and presion2 <= 93:
    print(chr(27)+'\033[93m'+"Prehipertension Alerta Amarilla.")
elif presion1 >= 138 and presion1 < 156 and presion2 >= 93 and presion2 <= 102:
    print("HTA Grado 1 Alerta Naranja.")
elif presion1 >= 156 and presion1 < 175 and presion2 >= 102 and presion2 <= 114:
    print(chr(27)+'\033[31m'+"HTA Grado 2 Alerta Roja.")
elif presion1 >= 175  and presion2 >= 114:
    print(chr(27)+'\033[31m'+"HTA Grado 3 Alerta Roja.")
elif presion1 >= 136  and presion2 < 92:
    print("Hipertension Sistolica Aislada Alerta Naranja.")
else:
    print(chr(27)+'\033[90m'+"No se puede determinar la categoria Alerta Gris.")
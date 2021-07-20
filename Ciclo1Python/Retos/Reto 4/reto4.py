# Reto 4 Uninorte, Mision tic 2022
# Realizado por Emanuel Rico Conde @ricocondee
# ID de estudiante: 200171465

sucursales = []
cantsucurs = tipomed = 0
while cantsucurs < 1 or tipomed < 1:
    cantsucurs, tipomed, pacientes = map(int, input().split())

for i in range(cantsucurs):
    sucursales.append(input().split())

for i in range(cantsucurs):
    for j in range(tipomed):
        sucursales[i][j] = int(sucursales[i][j])

datapac = []
for i in range(cantsucurs):
    datapac.append(0)

medent = []
for i in range(cantsucurs):
    medent.append([])
    for j in range(tipomed):
        medent[i].append(0)

for i in range(pacientes):
    sucursp, tmp, medso, presion1, presion2 = map(int,(input().split()))
    if sucursp <= cantsucurs and sucursp > 0 and tmp > 0 and tmp <= tipomed and medso >= 0:
        datapac[sucursp-1] = datapac[sucursp-1] + 1
        if presion1 < 72 and presion2 < 65:
            sucursales[sucursp-1][tmp-1] = sucursales[sucursp-1][tmp-1] - medso
            medent[sucursp-1][tmp-1] = medent[sucursp-1][tmp-1] + medso
        elif presion1 >= 72 and presion1 < 107 and presion2 >= 65 and presion2 <= 73:
            None
        elif presion1 >= 107 and presion1 < 124 and presion2 >= 73 and presion2 <= 81:
            None
        elif presion1 >= 124 and presion1 < 138 and presion2 >= 81 and presion2 <= 93:
            sucursales[sucursp-1][tmp-1] = sucursales[sucursp-1][tmp-1] - medso
            medent[sucursp-1][tmp-1] = medent[sucursp-1][tmp-1] + medso
        elif presion1 >= 138 and presion1 < 156 and presion2 >= 93 and presion2 <= 102:
            sucursales[sucursp-1][tmp-1] = sucursales[sucursp-1][tmp-1] - medso
            medent[sucursp-1][tmp-1] = medent[sucursp-1][tmp-1] + medso
        elif presion1 >= 156 and presion1 < 175 and presion2 >= 102 and presion2 <= 114:
            sucursales[sucursp-1][tmp-1] = sucursales[sucursp-1][tmp-1] - medso
            medent[sucursp-1][tmp-1] = medent[sucursp-1][tmp-1] + medso
        elif presion1 >= 175 and presion2 >= 114:
            sucursales[sucursp-1][tmp-1] = sucursales[sucursp-1][tmp-1] - medso
            medent[sucursp-1][tmp-1] = medent[sucursp-1][tmp-1] + medso
        elif presion1 >= 136 and presion2 < 92:
            sucursales[sucursp-1][tmp-1] = sucursales[sucursp-1][tmp-1] - medso
            medent[sucursp-1][tmp-1] = medent[sucursp-1][tmp-1] + medso

for i in range(cantsucurs):
    print(i+1)
    minimed = sucursales[i][0]
    maximed = sucursales[i][0]
    minient = min(medent[i])
    maxient = max(medent[i])

    pos1 = 1
    pos2 = 1
    for k in range(tipomed):
        if minimed > sucursales[i][k]:
            minimed = sucursales[i][k]
            pos1 = k + 1
        if maximed < sucursales[i][k]:
            maximed = sucursales[i][k]
            pos2 = k + 1
            
    dataprom = 0
    for j in range(tipomed):
        dataprom = dataprom + medent[i][j]
    promedio = dataprom/tipomed

    if datapac[i] == 0:
        promedio2 = 0
    else:
        promedio2 = dataprom/datapac[i]

    print(f"{pos1} {minimed}")
    print(f"{pos2} {maximed}")
    print(f"{minient:.2f} {promedio:.2f} {maxient:.2f}")
    print(f"{promedio2:.2f}")

minitipo1 = medent[0][0]
maxitipo1 = medent[0][0]
lastpos = 1
lastpost = 1
for x in range(cantsucurs):
    if minitipo1 > medent[x][0] :
        minitipo1 = medent[x][0]
        lastpost = x + 1
    if  maxitipo1 < medent[x][0]:
        maxitipo1 = medent[x][0]
        lastpos = x + 1
    
print(f"{lastpost} {minitipo1}")
print(f"{lastpos} {maxitipo1}")
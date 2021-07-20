# Reto 3 Uninorte, Mision tic 2022
# Realizado por Emanuel Rico Conde @ricocondee
# ID de estudiante: 200171465

p = 0
c = 0
sucursales = 0
listamedsucurs = []
listasucurs = []
while sucursales < 1:
    sucursales, pacientes = map(int, (input().split()))
for i in range(sucursales):
    listamedsucurs.append(0)
    listasucurs.append(0)

for j in range(sucursales):
    while listamedsucurs[j] < 1:
        listamedsucurs[j] = int(input())
        c += 1

dosispres1 = 4
dosispres2 = 0
dosispres3 = 0
dosispres4 = 2
dosispres5 = 4
dosispres6 = 8
dosispres7 = 16
dosispres8 = 12

for i in range(pacientes):
    sucursp, presion1, presion2 = map(int, (input().split()))
    if presion1 < 72 and presion2 < 65:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres1
            listasucurs[sucursp] += dosispres1
    elif presion1 >= 72 and presion1 < 107 and presion2 >= 65 and presion2 <= 73:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres2
            listasucurs[sucursp] += dosispres2
    elif presion1 >= 107 and presion1 < 124 and presion2 >= 73 and presion2 <= 81:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres3
            listasucurs[sucursp] += dosispres3
    elif presion1 >= 124 and presion1 < 138 and presion2 >= 81 and presion2 <= 93:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres4
            listasucurs[sucursp] += dosispres4
    elif presion1 >= 138 and presion1 < 156 and presion2 >= 93 and presion2 <= 102:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres5
            listasucurs[sucursp] += dosispres5
    elif presion1 >= 156 and presion1 < 175 and presion2 >= 102 and presion2 <= 114:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres6
            listasucurs[sucursp] += dosispres6
    elif presion1 >= 175 and presion2 >= 114:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres7
            listasucurs[sucursp] += dosispres7
    elif presion1 >= 136 and presion2 < 92:
        if sucursp <= sucursales and sucursp >= 1:
            sucursp -= 1
            listamedsucurs[sucursp] -= dosispres8
            listasucurs[sucursp] += dosispres8
    if c == sucursales:
        p += 1
    if p == pacientes:
        break
mini = listamedsucurs[0]
maxi = listamedsucurs[0]
posmini = 1
posmaxi = 1
for k in range(sucursales):
    if mini > listamedsucurs[k]:
        mini = listamedsucurs[k]
        posmini = k+1
    if maxi < listamedsucurs[k]:
        maxi = listamedsucurs[k]
        posmaxi = k+1
print(f"{posmini} {mini}")
print(f"{posmaxi} {maxi}")
for l in range(sucursales):
    porc = (listasucurs[l]/(listasucurs[l]+listamedsucurs[l]))*100
    print(f"{l+1} {porc:.2f}%")

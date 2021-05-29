#Ejercicios para llenar una matriz


""" n = int(input("Filas:"))
m = int(input("Columnas: "))
matriz = []
for i in range(n):
matriz.append([0]*m)
print(matriz[i]) """

""" n = int(input("Filas:"))
m = int(input("Columnas: "))
matriz = []
for i in range(n):
    matriz.append([0]*m)
for i in range(n):
    for j in range(m):
        matriz[i][j] = int(input("Matriz (%d, %d): " % (i, j)))
for i in range(n):
    for j in range(m):
        print(matriz[i][j],end=" ")
    print("\n") """

matriz = [[1,2,3,4,5],
          [6,7,8,9,0]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()
#Multiplicacion de matrices
n = int(input("filas:"))
m = int(input("Columna 2: "))
o = int(input("Columna 2: "))

a = []
b = []
c = []

for i in range(n):
    a.append([0]*m)
for i in range(m):
    b.append([0]*o)
    
for i in range(n):
    for j in range(m):
        a[i][j] = int(input("A[%s, %s]: "% (i+1, j+1)))
for i in range(m):
    for j in range(o):
        b[i][j] = int(input("B[%s, %s]: "% (i+1, j+1)))
for i in range(n):
    c.append([0]*o)
for i in range(n):
    for j in range(o):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
for i in range(n):
    r = []
    for j in range (o):
        r.append(c[i][j])
    print(r)

#Ejercicio 1
#Dada una matriz cuadrada A, construya un algoritmo que permita determinar si dicha matriz es simétrica.
#Se considera a una matriz simétrica si A[i,j] = A[j,i] y esto se cumple para todos los elementos i,j de la matriz

""" matrix = []
n = int(input("Tamaño de la matriz: "))
if (1 <= n and n <= 100):
    for i in range(n):
        matrix.append([])
        for j in range(n):
            elemento = input("matriz ({} {}): ".format(i+1, j+1))
            matrix[i].append(int(elemento))
    sw = True
    i = 0
    while (i < n and sw == True):
        j = 0
        while(i < n and sw == True):
            if (matrix[i][j] == matrix[i][j]):
                j += 1
            else:
                sw = False
        i += 1
    if(sw):
        print("La matriz es simetrica")
    else:
        print("La matriz no es simetrica")
else:
    print("La dimension de la matriz no es correcta") """


#Ejercicio 2
#Haga un algoritmo que calcule el producto escalar y vectorial de dos dos vectores de 3 elementos cuyos valores se
#introducen por pantalla.

""" a = 3*[0]
b = [0]*3

for i in range(3):
    a[i] = int(input("A({}): ".format(i+1)))
for i in range(3):
    b[i] = int(input("B({}): ".format(i+1)))
suma = 0
for i in range(3):
    p = a[i]*b[i]
    suma += p
print("El producto escalar es: ", suma)
x = a[1]*b[2] - a[2]*b[1]
y = -(a[0]*b[2] - a[2]*b[0])
z = a[0]*b[1] - a[1]*b[0]
print("El producto vectorial es: {}i {}j {}k".format(x, y, z)) """

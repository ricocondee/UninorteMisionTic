# Reto 5 Uninorte, Mision tic 2022
# Realizado por Emanuel Rico Conde @ricocondee
# ID de estudiante: 200171465

archivo = open("data.csv", mode='r', encoding='UTF-8') # Abrir archivo, (r)<--- en modo lectura (UTF-8)<-- formateado a unicode
lineas = archivo.readlines() # Leer todas las lineas y devolverlas en una lista
archivo.close() # cerrar archivo

campos = ['name', 'lastname', 'gender', 'city', 'state', 'id', 'medtype', 'quantity', 'pressure1', 'pressure2'] #Lista con las claves del diccionario
data = dict() #Diccionario vacio = {}

for i in campos: #For que llena el diccionario con los datos de la lista campos
    data[i] = [] # Agregando una lista vacia a cada clave del diccionario

for linea in lineas[1:]: #For que recorre las lineas de la lista "lineas" desde a posicion 1 a la ultima [1:]
    linea = linea[:-1].split(',') #Separa con una coma los datos en posicion de "linea" hasta e final menos 1 [:-1] ya que lo utimo es un \n
    for j in range(len(campos)): #For que recorre la longitud de la lista campos
        data[campos[j]].append(linea[j]) #Agregando a las listas vacias de las claves el recorrido de j

entrada = input().split() 
for k in range(len(entrada)): 
    entrada[k] = int(entrada[k]) #Convirtiendo el input a entero
entrada.sort() #Organiza en orden acendente

for sucursal in entrada: #recorre lo que hay en entrada
    totalmanes = 0  #------------------------------------⮯
    manesentr = 0
    totalmujeres = 0
    mujeresentr = 0
    medso = 0
    totalpac = 0
    desviacion1 = 0
    desviacion2 = 0
    medentr = 0 #Total de medicamentos entregados       #Inicializacion de variables
    minimo = int(data['quantity'][0])                   
    maximo = int(data['quantity'][0])
    nombre = data['name'][0]
    nombre2 = data['name'][0]
    genero = data['gender'][0]
    tipomed = data['medtype'][0]
    genero2 = data['gender'][0]
    tipomed2 = data['medtype'][0]
    lista = [] 
    nombresmf = [] 
    mf = []
    tpmedmf = [] #-----------------------------------------⮭

    for l in range(len(data['name'])): #---------------
        if sucursal == int(data["id"][l]):            #
                ciudad = data['city'][l]              #----- Filtro para obtener los datos por ciudad
                departamento = data['state'][l] #-----

                if 'm' == data['gender'][l]: #Si es hombre entra a verficar la presion s y d ⮯
                    totalmanes +=1
                    if int(data['pressure1'][l]) < 72 and int(data['pressure2'][l]) < 65:
                        manesentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                        
                    elif int(data['pressure1'][l]) >= 72 and int(data['pressure1'][l]) < 107 and int(data['pressure2'][l]) >= 65 and int(data['pressure2'][l]) <= 73:
                        None
                    elif int(data['pressure1'][l]) >= 107 and int(data['pressure1'][l]) < 124 and int(data['pressure2'][l]) >= 73 and int(data['pressure2'][l]) <= 81:
                        None
                    elif int(data['pressure1'][l]) >= 124 and int(data['pressure1'][l]) < 138 and int(data['pressure2'][l]) >= 81 and int(data['pressure2'][l]) <= 93:
                        manesentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 138 and int(data['pressure1'][l]) < 156 and int(data['pressure2'][l]) >= 93 and int(data['pressure2'][l]) <= 102:
                        manesentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 156 and int(data['pressure1'][l]) < 175 and int(data['pressure2'][l]) >= 102 and int(data['pressure2'][l]) <= 114:
                        manesentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 175 and int(data['pressure2'][l]) >= 114:
                        manesentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 136 and int(data['pressure2'][l]) < 92:
                        manesentr += 1
                        medentr += int(data['quantity'][l]) 
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l]) #------------- ⮭

                if 'f' == data['gender'][l]: #Si es mujer entra a verificar la presion s y d ⮯
                    totalmujeres +=1 
                    if int(data['pressure1'][l]) < 72 and int(data['pressure2'][l]) < 65:
                        mujeresentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 72 and int(data['pressure1'][l]) < 107 and int(data['pressure2'][l]) >= 65 and int(data['pressure2'][l]) <= 73:
                        None
                    elif int(data['pressure1'][l]) >= 107 and int(data['pressure1'][l]) < 124 and int(data['pressure2'][l]) >= 73 and int(data['pressure2'][l]) <= 81:
                        None
                    elif int(data['pressure1'][l]) >= 124 and int(data['pressure1'][l]) < 138 and int(data['pressure2'][l]) >= 81 and int(data['pressure2'][l]) <= 93:
                        mujeresentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 138 and int(data['pressure1'][l]) < 156 and int(data['pressure2'][l]) >= 93 and int(data['pressure2'][l]) <= 102:
                        mujeresentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 156 and int(data['pressure1'][l]) < 175 and int(data['pressure2'][l]) >= 102 and int(data['pressure2'][l]) <= 114:
                        mujeresentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 175 and int(data['pressure2'][l]) >= 114:
                        mujeresentr += 1
                        medentr += int(data['quantity'][l])
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l])
                    elif int(data['pressure1'][l]) >= 136 and int(data['pressure2'][l]) < 92:
                        mujeresentr += 1
                        medentr += int(data['quantity'][l]) 
                        lista.append(int(data['quantity'][l]))
                        nombresmf.append(data['name'][l]+ ' ' + data['lastname'][l])
                        mf.append(data['gender'][l])
                        tpmedmf.append(data['medtype'][l]) #---------------------------------- ⮭

                if minimo > int(data['quantity'][l]):
                    minimo = int(data['quantity'][l])
                if maximo < int(data['quantity'][l]):   
                    maximo = int(data['quantity'][l])

                medso += int(data['quantity'][l]) # Total de medicamentos solicitados
                totalpac += 1 #Total de pacientes
                totalentr = manesentr + mujeresentr #Total de pacientes a los que se les entregaron medicamentos

    promedio1 = medso/totalpac #---------------------------------------⮯
    promedio2 = medentr/totalentr
    minimonom = lista[0]
    maximonom = lista[0]
    for o in range(len(data['name'])):
        if sucursal == int(data['id'][o]):
            desviacion1 += ((int(data['quantity'][o])-promedio1))**2

    for p in range(len(lista)):                                         #Sacando la desviacion estandar muestral
            desviacion2 += ((lista[p])-promedio2)**2
            if minimonom > lista[p]:
                minimonom = lista[p]
                nombre = nombresmf[p]
                genero = mf[p]
                tipomed = tpmedmf[p]
            if maximonom < lista[p]:   
                maximonom = lista[p]
                nombre2 = nombresmf[p] 
                genero2 = mf[p]
                tipomed2 = tpmedmf[p]

    desviacion1 = (desviacion1/(totalpac-1))**(1/2)
    desviacion2 =  (desviacion2/(totalentr-1))**(1/2) #------------⮭

    print(f"{sucursal} {ciudad} {departamento}") #------Mostrar info-⮯
    print("patients")
    print(f"male {totalmanes}")
    print(f"female {totalmujeres}")
    print(f"total {totalpac}")
    print("medicine quantity")
    print(f"mean {promedio1:.2f}")
    print(f"std {desviacion1:.2f}")
    print(f"min {minimo}")
    print(f"max {maximo}")
    print(f"total {medso}")
    print("scheduled patients")
    print(f"male {manesentr}")
    print(f"female {mujeresentr}")
    print(f"total {totalentr}")
    print("scheduled medicine quantity")
    print(f"mean {promedio2:.2f}")
    print(f"std {desviacion2:.2f}")
    print(f"min {minimonom} {nombre} {genero} {tipomed} ")
    print(f"max {maximonom} {nombre2} {genero2} {tipomed2}")
    print(f"total {medentr}") 
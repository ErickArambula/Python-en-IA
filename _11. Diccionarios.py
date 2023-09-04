#******************************DICCIONARIOS*********************************

teclado1 = {
    "Categoria": "Teclados",
    "Modelo" : "Patito pro x 300 mil millones",
    "Precio" : "40 000 000"
    }                                          #para almacenar strings mas complejos y mas sencillo que en una lista 

teclado2 = {
    "Categoria": "Teclados",
    "Modelo" : "Escribesolo 5000 kit marker",
    "Precio" : "20"
    }

consulta = teclado1.get("Modelo"), teclado1["Precio"], teclado2["Modelo"], teclado2["Precio"]    #".get"   otra manera de obtener ese dato
print(consulta)

muestraTeclado = dict(teclado1)       #"dict(diccionario)"  para mostrar todo el diccionario 
print(muestraTeclado)

#*********************************************************************************

print("\n", teclado1)                #una manera de imprimir todo el diccionario 

#**********************MODIFICAR ALGUN VALOR DEL DICCIONARIO************************

print(teclado1.get("Precio"))
teclado1["Precio"] = "85"              #para modificar algun valor del diccionario 
print(teclado1.get("Precio"))

#***********************************FOR CON DICCIONARIOS*******************************

for x in teclado2:          #En este caso solo imprime las categorias SIN contar las categorias 
    print(x)

for w in teclado2:          #este otro imprime solo los atributos y no las categorias
    print("\n", teclado2[w])

for z in teclado1.values():    #".values" tambien para imprimir los atributos sin las categorias
    print(z)

for e, r in teclado2.items():          #.items para imprimir los dos valores del diccionario, atributos y categorias 
    print(e,":",  r)
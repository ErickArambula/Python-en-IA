
teclado1 = {
    "Categoria": "Teclados",
    "Modelo" : "Patito pro x 300 mil millones",
    "Precio" : "40 000 000" ,
    "ID" : "001"
    }                                          

teclado2 = {
    "Categoria": "Teclados",
    "Modelo" : "Escribesolo 5000 kit marker",
    "Precio" : "20"
    }

#teclado1.clear()       //Deja sin ningun valor al diccionario mas que unos corchetes "{}" sirve para que el codigo no de excepcion de compilacion
#print(teclado1)

teclado1["color"] = "negro"    #agregar un acategoria con atributo al diccionario 
print(teclado1)

#*************************Hacer copia del diccionario o agragar otro**********************

tecladoCopia = teclado2.copy()     #.copy para hacer una copia del diccionario 
print(tecladoCopia)

tecladoCopia1 = dict(teclado2)      
print(tecladoCopia1)

teclado3 = dict(Categoria = "Teclados",
                Modelo = "escribeloco 3500 tausen",        #agregar toda otra categoria
                Precio = "GRATIS")
print(teclado3)

#****************************AUTORRELLENAR LOS DICCIONARIOS**********************************************

teclado4 = ("Categoria", "Modelo", "Precio")
teclado5 = ("Categoria", "Modelo", "Precio")
vacia = 'Valor vacio.'

teclado4 = dict.fromkeys(teclado4, vacia)     #Asigna la variable "vacia" a todos los espacios del diccionario 
print(teclado4)

teclado5 = dict.fromkeys(teclado5, "Nada.")  
print(teclado5)

#***************************UPDATE DICCIONARIOS************************

teclado5.update({"color" : "pelucas"})        #actualiza las categorias o atrubutos seleccionados
print(teclado5)

#***********************

if "ID" in teclado1:
    print("El producto tien ID")
else:                                         #Buscar el ID en el diccionario 
    print("No encontrado, reingresa el ID")

#****************************DICCIONARIOS ANIDADOS********************

teclados = {
"tecladox" : {
    "Categoria": "Teclados",
    "Modelo" : "perro con croquetas infinitas",
    "Precio" : "nada de nada" ,
    "ID" : "004"
    },                                          

"tecladoy" : {
    "Categoria": "Teclados",
    "Modelo" : "Escribesolo 5000 kit marker",
    "Precio" : "20"
    }
}
print(teclados)
print("\n", len(teclados),"\n")
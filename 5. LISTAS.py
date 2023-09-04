#********************************LISTAS****************************

laptops = ["Dell","Acer","Apple", "HP", "lenovo", "Xiaomi", "Asus", "Msi"]     #Si los valores fueran enteros no necesita comillas

print("\n",laptops)
print(laptops[3])    #print(nombre de la lista[elemento a imprimir])

#***********Si no se la posicion del ultimo elemento*************************

print("El ultimo elemento de la lista es: " + laptops[-1])       # "ista[-1]" para acceder al ultimo elemento, acceder con su posicion negativa
print("El penultimo elemento de la lista es: " + laptops[-2])  

#*********************ELIMINAR elementos de la lisa**************************

del laptops[1]             #".del lista[elemento a eliminar]" para eliminar un elemento seleccionado de la lista 
print (laptops)

laptops.remove("Dell")     #".remove" es otro metodo para eliminar por medio del velor que quieres eliminar
print(laptops)

print("\n")
colores = ["rojo", "amarillo", "verde", "azul", "morado", "naranja", "cafe"]
guardaLista = colores.pop(0)     #".pop(elemnto a eliminar)"  es para eliminar un elemento pero guardarlo en la variable "guardaLista"
print(colores)
print("El color eliminado de la lista y guardado es el: " + guardaLista, "\n")

#******************AÑADIR ELEMENTO A LA LISTA*****************************

colores.append("termopilas")    #"lista.append(valor a agregar)"    con esta funcion siempre se agregaran al FINAL las listas
print("\n",colores,"\n")

colores.insert(0, "mapache")       #"lista.insert(posicion, valor a agregar)"  para agregar a la lista en la posicion deseada
print("\n",colores,"\n")

#**********************ORDENAR LISTAS ALFABETICAMENTE*************************

colores.sort()                 #estos cambios son permanentes, la lista se modificara cambiando su orden
print("\n",colores,"\n")      

colores.sort(reverse=True)     #para ordenar los elementos de la lista inversos al alfabeto, tambien se modifica su posicion permanentemente
print("\n",colores,"\n")

print(sorted(colores))         #No se modifica su posicion, solo se ordena para la instruccion de impresion

#**********************CONTAR ELEMENTOS DE LA LISTA********************************

print(len(laptops))
print("\n")                       #len(lista) para contar los elementos de la lista
print(len(colores))

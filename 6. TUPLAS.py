#***************************TUPLAS*****************************

lista = [1,2,3,4,5,6,7,8]       #en una lista los elementos pueden variar o modificarse 

tupla = (1,2,3,4,5,6,7,8)       #en la tupla los elementos son permanentes 
print(lista, "\n", tupla)

print(tupla[7])                 #para llamar elementos de la tupla 

#*******************

tupla2 = (10,20,30,"El resultado de la operacion es: ")
print(tupla2[3], tupla2[0] + tupla2[2])      #para concatenar y mezclar tipos de datos en la tupla 

#*******************

tupla3 = (10,)     #si no ponemos la coma el programa no detecta que es una tupla, solo seria una variable con un valor asignado 

#***********************CONVERTIR TUPLAS A LISTAS Y VICEVERSA*************************

tupla4 = tuple(lista)    #estamos almacenando esa lista dentro de una tupla      
print(tupla4)

lista2 = list(tupla4)
print(lista2)
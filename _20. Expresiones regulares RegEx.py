#                Expresiones RegEx
#***************************************************
#              Funciones 
#   findall()
#   search()
#   split()
#   sub()
#***************************************************

import re

#                * search() *    

texto = "Bienvenidos a Inteligencia artificial"
busqueda = re.search("i", texto)            #busca el primer caracter que coincida con el seleccionado "i" en este caso
print(busqueda)                             #Muestra su posicion donde inicia y donde termina 

busqueda1 = re.search("Bienvenidos", texto) #busca el primer caracter que coincida con el seleccionado "Bienvenidos" en este caso
print(busqueda1) 

#                * findall() *    

texto1 = "pedrito clavo un clavito en pablito"
busqueda2 = re.findall("i", texto1)            #busca todos los caracteres que coincidan con el seleccionado "i" en este caso
print(busqueda2) 

#                * split() *    

texto2 = "Quien no conoce su historia esta condenad a repetirla - Walter Bazar"
busqueda3 = re.split("no", texto2)            #omite todos los caracteres que coincidan con el seleccionado "no" en este caso
print(busqueda3) 

busqueda4 = re.split(" ", texto2, 2)          #se especifica la cantidad de resultados que admite el patron de busqueda "2" en este caso     
print(busqueda4)

#                * sub() *    

busqueda4 = re.sub("no", "---", texto2) #remplaza todos los caracteres que coincidan con el seleccionado " " en este caso por el segundp especificado "---" en este caso
print(busqueda4) 

busqueda5 = re.sub(" ", "+", texto2, 7) #se especifica la cantidad de resultados que admite el patron de busqueda "7" en este caso     
print(busqueda5)


#*****************METACARACTERES, SECUENCIAS ESPECIALES Y SETS****************
#
# En el siguiente link se explica este tema extra 
# https://www.programacionfacil.org/cursos/python_basico/capitulo_50_secuencias_especiales_metacaracteres_sets_python.html
#
#*****************************************************************************
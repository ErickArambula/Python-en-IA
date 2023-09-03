#***************************************Declaracion de strings**************************************

"Esto es un tring"     #De estas dos maneras se declara un string
'Esto es un tring'

texto = "Esto es un 'stirng'"  
texto2 = 'Esto es un "string"'
print (texto, texto2)

#****************************************Concatenar Strings***************************************************

palabra1 = "Rayo"     
palabra2 = "MQueen"         #Las diferentes maneras de concatenar strings sin necesidad de guardarlo en un avariable 

nombreCanal = palabra1 + "  " + palabra2 + ". "

print(nombreCanal)
print("Este es el canal" + " de programacion Facil.")

#****************************************Formato de texto para strings**********************************

tipo1 = "erick alejandro arambula saldana"
tipo1 = tipo1.title()      #".title"  Pone en mayusculas las primeras letras de un apalabra
print(tipo1)               #Se puede hacer dentro de la funcion "print(tipo1.title())""

tipo2 = "erick alejandro arambula saldana"
print(tipo2.upper())       #".upper"  Convierte todo el texto en MAYUSCULAS 

print("PRograMaCioN".lower())    #".lower"  Convirte todo el texto en minusculas

#***********************************Saltos de linea y tabulaciones*************************************

print("\n\n\njitomate\nAguacate\nJamon\nHuevo")        # "\n" = Salto de linea 

print("\n\nLista de las compras:\n\tHuevo\n\tAguacate\n\tetc...\n\n")
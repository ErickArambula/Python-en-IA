#********************WHILE*****************************

x = 1

while x < 11:
    print(x)
    if x == 5:           #Romper el bucle while aunque no se cumpla la condicion 
        break
    x += 1    #incrementa la variable X una vez cada ciclo

else:
    print("Saliendo del bucle While\n")   #para ejecutar otra instruccion al salir del ciclo (No entra por el BREAK)

#*********************************************************
frase = "Lo que escribas lo repito:"
frase += "\nIntroduce el comando 'salir' para cerrar el programa.\n"

mensaje = ""

while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)

#********************************CONTINUE*********************************

y = 0
while y < 10:
    y += 1
    if y == 5 or == 7:
        continue          #No toma en cuenta al 5 y 7 por la condicion 
    print(y)
    
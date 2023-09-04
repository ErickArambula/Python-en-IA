#*****************************FOR******************************

cursos = ["Python", "JavaScript", "COBOL", "HTML"]    

for x in cursos:               #se ejecutara el ciclo y recorrera e imprimira toda la lista "cursos"
    if x == "COBOL":
        continue               #se salta el string del condicional y sigue con los demas, tambien podemos utilizar un "BREK" (sale del ciclo) o "PASS" (no entra al ciclo)
    print(x)

#******************************RANGE************************************
for y in range(5,25,):          #para darle rango al for, donde empieza, donde termina y el incremento (5,25,2)
    print(y)

#**********************************************************************

print("\nLista de numeros: \n")
numeros = [2,4,8,16,32,64,128]

for z in range(len(numeros)):
    print("Numero de operacion -> ", z, "Multiplicacion ->", numeros[z], "Resultado: ->",numeros[z] * numeros[z])

#**************************FOR ANIDADO*********************

num1 = ["1","2","3"]
num2 = "2"

for k in num1:                
    for l in num2:
        print(k + l)
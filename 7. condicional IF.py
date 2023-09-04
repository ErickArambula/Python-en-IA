#*******************************CONDICIONAL IF************************
#    CONSEJOS
#  1.Cuidar las sangrias
#  2.Separar los operadores para no confundirlos
#  3.  print("....") if x > y else print("....")     //Manera de escribir if else ejn una sola linea 
#  4.  if x > y:
#           pass     //Para que el programa lo ignore 
#
#*********************************************************************

num1 = 10
num2 = 20          # "=" es para asignar valor,  "==" es para compaar variables

if num1 == num2:                         #solo puden ser condiciones booleanas (verdadero/falso)
    print("las cvariables son iguales")

if num1 != num2:                         
    print("\nlas variables son diferentes\n")

#*************************IF_ELSE***************************************

edad = 18

if edad >= 18:
    print("Puedes acceder, eres mayor de edad.\n")

else:
    print("No puedes acceder, eres menor de edad.")     #como sabemos entra en caso de no cumplirse el if 

#*******************************************************************

edad = int(input("Cual es tu edad?\n"))       #edad=tipo de dato(input("string")) entrada de datos que se almacena en la variable edad

if edad <=0:
    print("No valido.")

elif edad >= 1 and edad <=17:                 #se le ponen mas condiciones 
    print("Menor de edad.")

elif edad <= 100:
    print("mayor de edad.")
else:
    print("ya estas grande eh.")

#**************************COMPROVAR DATOS EN LISTAS Y TUPLAS************************************

entrada = input("Introduce el nombre de un navegador: \n")

navegadores = ['chrome', 'firefox', 'opera', 'safari']
if entrada in navegadores:
    print("Si esta en la lista")
else:
    print("No esta en la lista")

#print('edge' in navegadores)           #compara si este string se encuentra en tu tupla o tu lista y lo imprime 






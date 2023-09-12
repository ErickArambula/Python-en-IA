#*********Comando para mostrar la fehca al momento de ejecucion del programa**********

import datetime

fecha = datetime.datetime.now()         
print(fecha)

#*******************Cambiar el formato en que se presenta la fecha***********************

fecha1 = datetime.datetime(2020, 9, 29, 10, 50, 45)         
print(fecha1)

fecha2 = datetime.datetime.now()       
print("Año: ", fecha2.year)
print("Mes: ", fecha2.month)
print("Dia: ", fecha2.day)
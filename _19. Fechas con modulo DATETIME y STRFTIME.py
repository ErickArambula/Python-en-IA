#                              * DATETIME *
#*********Comando para mostrar la fehca al momento de ejecucion del programa**********

import datetime, locale              # LOCALE es para traducir el idioma 

fecha = datetime.datetime.now()         
print(fecha)

#*******************Cambiar el formato en que se presenta la fecha***********************

fecha1 = datetime.datetime(2020, 9, 29, 10, 50, 45)         
print(fecha1)

fecha2 = datetime.datetime.now()       
print("Año: ", fecha2.year)
print("Mes: ", fecha2.month)
print("Dia: ", fecha2.day)

#                              * STRFTIME() *
#*********************************************************************************
#  %d - Dia del mes / 01-31
#  %a - Dia de la semana (corto) /mi.
#  %A - Dia de la semana (entero) /miercoles
#  %w - Dia de la semana (numero) /0-6
#  %b - Mes (corto) / mar
#  %B - Mes (entero)/ marzo
#  %m - Numero del mes/01-12
#  %y - año (corto)/23
#  %Y - año (entero)/2023
#  %H - Hora/00-23
#  %I - Hora / 00-12
#  %p - AM-PM
#  %M - Minutos / 00-59
#  %S - Segundos / 00-59
#  %f - Microsegundos / 000000-999999
#  %x - Fecha local/ 18/03/2023
#  %X - Hora local/ 16:50:39
#
#**********************************************************************************
locale.setlocale(locale.LC_ALL, "es-ES")     #TRADUCIR AL ESPAÑOL

fecha3 = datetime.datetime.now()       #Podriamos tambien poner una fcha personalizada en lugar de ".now"      
print(fecha3.strftime("%A"))
print(fecha3.strftime("%H"))
print(fecha3.strftime("%M"))
print(fecha3.strftime("%X"))

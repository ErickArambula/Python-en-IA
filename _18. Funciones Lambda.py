import math

def area (radio):
    resultado = round(math.pi * radio * radio, 3)     #ROUND es para especificar los decimales que quieres utilizar "3" en este caso
    print(resultado)

area(2)

#************** LAMBDA *****************

area = lambda radio: round(math.pi * radio * radio, 5)  #ROUND redondea segun los decimales especificados "5" en este caso
print(area(2))
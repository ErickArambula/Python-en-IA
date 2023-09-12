#*******************VARIABLE LOCAL Y FUNCION ANIDADA*****************************

def funcion1():
    variable1 = "Variable dentro de la funcion."       #Esta variable es local "Solo existe en la ("funcion1")"
    print(variable1)

    def funcion2():        #Esta es una funcion anidada
        variable1 = "He cambiado el valor de la funcion"
        print(variable1)

    funcion2()          #Se llama la funcion2 DENTRO de la funcion 1 por que solo existe ahi. 

funcion1()

#************************VARIABLE GLOBAL***********************************

variable3 = "Variable fuera de una funcion."

def funcion3():
    print(variable3)

def funcion4():
    variable3 = "Variable dentro de la funcion"     #la variable global MANTENDRA su valor y la local se trata como otra variable
    print(variable3)

funcion3()
funcion4()

print(variable3)

#************************DECLARAR VARIABLE GLOBAL EN UN AFUNCION*****************

num1 = 45

def funcion5():
    global num1 
    num1 = 78              #  NO SE PUEDE DECLARAR Y ASIGNAR VALOR EN EL MISMO RENGLON 

funcion5()
print(num1)
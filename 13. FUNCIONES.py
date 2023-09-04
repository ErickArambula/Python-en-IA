#*********************************FUNCIONES*************************************

#****************SIN PARAMETROS****************
def saluda():
    print("Asi nomas quedo mi primera funcion.\n")

saluda()

#****************CON PARAMETROS***********

print("La familia simpson\n")

def familiasS(nombre, parentesco):                 #Necesario devolverle dos argumentos a la funcion
    print(nombre + " Simpson " + parentesco)

familiasS("Homer", " Padre")
familiasS("Marge", " Madre")
familiasS("Lisa", " Hija")
familiasS("Bart", " Hijo")
familiasS("Maggie", " Hija")

#*********************ARGUMENTOS ARBITRARIOS*******************

def alumnos(*args):       #"*args" se escribe por convencion, funcionaria con cualquier otra palabra
    print("El ultimo alumno es: " + args[3] + " y el primero es " + args[0] + ".")

alumnos("Andres", "Jose", "Manuel", "Juanita")

#*******************ARGUMENTOS ARBITRARIOS + FIJOS*********************

def alumnos_profes(prof,sustituto,*args):              #es necesario mandarle los primeros dos argumentos, slavo el tercero por "*args"
    print("\nProfesor: ", prof, "\nSustituto: " + sustituto )
    for x in args:
        print("Alumno: " + x)

lista_alumnos = ["Andres1", "Jose1", "Manuel1", "Juanita1"]

alumnos_profes("Antonio", "Amanda", *lista_alumnos)    #los argumentos se mandan al llamar la funcion

#********************DICCIONARIOS ARBITRARIOS**************************

def colores(color1, color2, color3, color4):
    print ("Este es el color " + color3 + ".")

colores(color1 = "Rojo", color2 = "Morado", color3 = "Verde", color4 = "Azul")     #se asignan valores a las variables en esta tupla

#*********************************KWARGS*******************************

#En diccionarios los elementos se llaman "Keywords" y sus valores "Values"

def perros (**kwargs):         #"**kwargs" tambien por convencion  (Keyword arguments ------> KWARGS) 
    print("Este es el perro magico: " + kwargs["perro3"] + ".")

perros(perro1 = "salchicha", perro2 = "pastor velga", perro3 = "Chihuahua")

#********************************

def suma (x, y):
    return x + y

total = suma(10, 10)
print(total)


def resta (x, y):
    return x - y

total = resta(10, 10)
print(total)


def mult (x, y):
    return x * y

total = mult(10, 10)
print(total)


def division (x, y):
    return x / y

total = division(10, 10)
print(total)

#******************************FUNCIONES CON PASS**************************

def calcetines():
    pass

#****************cambiando valores definidos de una funcion*****************

def pantalones (normales = "Zara"):
    print("Los peores pantalones son de: " + normales)

pantalones("American Eagle")
pantalones()
pantalones("Cuiado con el dog")






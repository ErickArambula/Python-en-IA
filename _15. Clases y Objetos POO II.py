#*****************************Uso de __INIT__********************************

class Usuarios():

    def __init__(self, nombre, pin):           # __init__ : se usa para definir parametros u argumentos por defecto para la funcion 
        self.nombre = nombre
        self.pin = pin

    def saludo(self):
        print("Saludos " + self.nombre + ". Iniciaste sesion correctamente.")

    def despedida(self):
        print(self.nombre + ", cerraste la sesion.")

usuario1 = Usuarios("Javier", "1234")
usuario2 = Usuarios("Julia", "3692")

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()

#**********************CAMBIAR VALORES EN LOS ARGUMENTOS DEL OBJETO*********************

class Personas:
    def __init__ (persona,nombre,edad):
        persona.nombre = nombre        #No es necesario que sea especificamente la palabra SELF ya que son diferentes para cada funcion
        persona.edad = edad

    def muestra_datos(datos):
        print("El usuario es: " + datos.nombre, datos.edad)            #De nuevo cambiamos "SELF" por DATOS (nosotros elegimos)

persona1 = Personas("Julian", 65)
persona1.muestra_datos()

persona1.edad = 12000
persona1.muestra_datos()

#******************USAR PASS en clases***************

class nombreClase ():        #Asi podriamos compilar nuestoro codigo 
    pass

#*********************BORRAR OBJETOS O DATOS DEL OBJETO******************

class Relojes():
    def __init__ (swatch, tipo, precio):
        swatch.tipo = tipo
        swatch.precio = precio

    def muestra_datos(self):
        print("El reloj es: " + self.tipo, self.precio)

reloj1 = Relojes("Rolex", 82000)

reloj1.muestra_datos()

del reloj1.precio         #Para eliminar se usa DEL
del reloj1                #Para eliminar todo el objeto

print(reloj1.tipo, reloj1.precio)
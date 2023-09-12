#******************************HERENCIA DE CLASES********************************

class Usuarios:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def muestra_datos(self):
        print("El usuario es: " + self.nombre + ",  y tiene: ", self.edad)

usuario1 = Usuarios("Enrrique", 9859)
usuario1.muestra_datos()

class Usuarios_premium(Usuarios):
    pass

usuario2 = Usuarios_premium("Elvira", 9)
usuario2.muestra_datos()

#**************************HEREDAR PROPIOEDADES __INIT__ **************************

class Personas:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def muestra_datos(self):
        print("El usuario es: " + self.nombre + ",  y tiene: ", self.edad)

persona1 = Personas("Enrrique", 9859)
persona1.muestra_datos()

class Personas_premium(Personas):
    def __init__(self, nombre, edad, instagram):
        Personas.__init__(self,nombre,edad)       #para poder utilizar __init__ y aun heredar las propiedades de la clase principal  
        self.instagram = instagram
    
    def muestra_datos_premium(self):
        print("El usuario es: " + self.nombre + ",  y tiene: ", self.edad, "años. Su instagram es: ", self.instagram)

persona2 = Personas_premium("Elvira", 9, "elvi_23")
persona2.muestra_datos_premium()

    
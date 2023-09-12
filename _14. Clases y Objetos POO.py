class Naves():
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Plateado"
    motores = 4
    activada = False
    compuerta_princial = False
    sistema_defensa = True
    autodestruccion = False

    def encender(self):            # SELF: hace referencia a cualquier objeto que hayamos creado por eso es NECESARIO en python
        self.activada = True 

    def apagar(self):
        self.activada = False

    def estado_nave(self):
        if(self.activada):
            return "La nave esya ready."
        else:
            return "Ya valio madres la nave"

    def abrir_compuerta(self):
        self.compuerta_proncioal = True

    def activar_autodestruccion(self):
        self.autodestruccion = True
        mensaje = "Protocolo de autodestruccion activado..."
        print(mensaje)

    def apagar_defensa(self):
        self.sistema_defensa = False

    def estado_defensa(self):
        if(self.sistema_defensa):
            return "El sistema de defensa esta activado."
        else:
            return "¡Peligro! el sistema de defensa esta desactivado."
        
    
#*****Se crea el primer objeto de nivel que pertenece a la calase naves**********

nave1 = Naves()

#comandos o LLAMADAS al objeto

#Enciende la nave.
print(nave1.estado_nave())

nave1.encender()

print(nave1.estado_nave())

#comprueba estado de sistema de defensa
print(nave1.estado_defensa())

nave1.apagar_defensa()

print(nave1.estado_defensa())

#Apaga la nave
nave1.apagar()

print(nave1.estado_nave())









#******************** TRY y EXCEPT*********************

variable = "Correcto."

try:
    print(variable)
    print(variable2)

except:
    print("Hay un error")

#*************** Ejemplo elaborado ***************

reinicio = True

while reinicio:
    try:
        num1 = int(input("Introduce un numero para multiplicar: "))
        num2 = int(input("Introduce otro numero: "))
    except ValueError:
        print("Valor introducido no valido: ")
    else:
        print("El resultado es: ", num1 * num2)
    finally:
        pregunta = input("¿Quieres continuar? Presiona 'S'\nQuieres salir presiona 'N'\n")
    if pregunta == "N":
        reinicio = False
    else:
        print("Sigamos entonces ")
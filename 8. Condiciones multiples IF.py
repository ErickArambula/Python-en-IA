print("\nSaludos compi, ¿Que desea comprar?\n\n"+
      "items disponibles:\n\n"+
      "Espadas:\n\n"+
      "1-Espada nivel 1: 150 monedas.\n2-Espada nivel 2: 1200 monedas.\n\n"+
      "Escudos:\n\n"+
      "3-Escudo nivel 1: 150 monedas.\n4-Escudo nivel 2: 1200 monedas.\n\n")

comprar = [8]
dinero = 1500
espadaLV1 = 150
espadaLV2 = 1200
escudoLV1 = 120
escudoLV2 = 1200

if 0 in comprar or comprar == []:
    print("No valido, Dame un numero del 1 al 4.")
if 1 in comprar:
    dinero = dinero - espadaLV1
if 2 in comprar:
    dinero = dinero - espadaLV2
if 3 in comprar:
    dinero = dinero - escudoLV1
if 4 in comprar:
    dinero = dinero - escudoLV2
else:
    print("ES nomas del 1 al 4 eh!")

if dinero < 0:
    print("No te alcanza mi pa")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te quedan " + str(dinero) + " monedas pa.")
    print("Se añadio el/los objeto/s a tu inventario.")


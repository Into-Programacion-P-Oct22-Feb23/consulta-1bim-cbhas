nombre = input("Escribe tu nombre:\n")
peso = float(input("Escribe tu peso en kilogramos(Kg):\n"))
altura = int(input("Escribe tu altura en centímetros(cm)):\n"))

masaCorporal = round(peso / ((altura / 100) ** 2), 2)  #

print(nombre + ", tu Índice de Masa Corporal (IMC) es:", masaCorporal)

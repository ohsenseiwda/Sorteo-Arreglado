import random
import os


porcentaje_30 = 30
porcentaje_20 = 20
porcentaje_50 = 50

persona_1 = "Pedro"
persona_2 = "Juan"
persona_3 = "Luis"


def sortear():
	os.system('clear')
	print(input("Toca Enter para sortear"))
	num_aleatorio = random.randint(1,100)
	return num_aleatorio
	
def operacion(num):
	
	#Pedro tiene 30% chances de ganar
	if num < 30:
		print("GANÓ "+ str(persona_1))
		
	#Juan tiene un 20% chances de ganar
	elif num >= 30 and num <= 50:
		print("GANÓ "+ str(persona_2))
		
	#Luis tiene un 50% chances de ganar
	elif num >= 50:
		print("GANÓ "+ str(persona_3))
	
	#Este input solo es para hacer una pausa al programa
	input()


while True:
	numero_sorteado = sortear()
	operacion(numero_sorteado)



# Bueno así de esta manera LUIS será el que más
# chances tendra de ganar el sorteo, ya que tiene
# un 50% de probabilidad de ganar más que el resto.
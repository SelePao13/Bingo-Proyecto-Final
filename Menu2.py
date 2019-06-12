jugadores = int(input("Digite numero de jugadores: "))
nombre = input("Ingrese su nombre: ")
cartillas = int(input("Digite numero de cartillas: "))

def pedirNumeroEntero():

	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input("Introduce opcion: "))
			correcto=True
		except ValueError:
			print('Error, introduce opcion')
	
	return num

salir = False
opcion = 0

while not salir:

	print ("1. Jugar")
	print ("2. Resultado")
	print ("3. Reiniciar juego")
	print ("4. Finalizar juego")
	
	print ("Elige una opcion")

	opcion = pedirNumeroEntero()

	if opcion == 1:
		import random
		for x in range(1):
			print("Su bolilla es", random.randint(1,80))
	elif opcion == 2:
		import random  
		bolillas=[random.randint(1, 80)]
		i=1
		while i<15:
			x=random.randint(1,80)
			for j in range(0, len(bolillas)):
				if bolillas[j]==x:
					break
			else:
				bolillas.append(x)
				i+=1
				print("Las bolillas son:",bolillas)
	elif opcion == 3:
		print("Reiniciar juego")
	elif opcion == 4:
		salir = True
	else:
		print ("Introduce un opcion 1 y 3")

print ("Fin")
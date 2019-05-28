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
		print ("Jugar")
	elif opcion == 2:
		print ("Resultado")
	elif opcion == 3:
		print("Reiniciar juego")
	elif opcion == 4:
		salir = True
	else:
		print ("Introduce un opcion 1 y 3")


print ("Fin")
	
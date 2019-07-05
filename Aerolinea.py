import os 
import math 
import getpass
from time import sleep

contadorturista = 0
contadornegocio = 0
contadorprimeraclase = 0
contadortarjeta = 0
contadorefectivo = 0

class Cliente:

	def __init__(self,nombre,apellido,edad,usuario,contraseña):

		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
		self.usuario=usuario
		self.contraseña=contraseña

class Compra:

	def __init__(self,vuelocompra,boletoscompra,clasecompra,pagocompra):

		self.vuelocompra=vuelocompra
		self.boletoscompra=boletoscompra
		self.clasecompra=clasecompra
		self.pagocompra=pagocompra

while True:

	print("\t\t------ SISTEMA DE VENTAS ------\n\n")
	print("1. Administrador\n")
	print("2. Cliente\n")
	print("3. Salir\n")

	op = int (input ("Ingresa una de las opciones anteriores: "))

	if op == 1:

		while True:

			print("\n------ Administrador ------\n\n")
			print("1. Ingresar\n")
			print("2. Regresar\n")
			
			opa = int (input("Elige alguna de las opciones: "))

			if opa == 1:

				nombre_ao1 = "Edgar"
				apellido_ao1 = "Cisneros"
				nombre_ao2 = "Citlali"
				apellido_ao2 = "Bruce"
				contraseña_ao1 = "12345"
				contraseña_ao2 = "54321"

				nombre_a = input("Administrador: ")
				contraseña_a = getpass.getpass ("Contraseña: ")

				
				if ((nombre_a == nombre_ao1 and contraseña_a == contraseña_ao1) or (nombre_a == nombre_ao2 and contraseña_a == contraseña_ao2)):

					while True:	

						if nombre_a == nombre_ao1:
								
							print("\n\nBienvenido, {0}\n".format(nombre_ao1))

						elif nombre_a == nombre_ao2:
							
							print("\n\nBienvenido, {0}\n".format(nombre_ao2))

						
						print("\t\t------ SISTEMA DE VENTAS ------\n\n")

						print("1.Ingresar no. máximo de vuelos\n")
						print("2.Ingresar vuelos\n")
						print("3.Listas vuelos\n")
						print("4.Cancelar vuelos\n")
						print("5.Actualizar vuelos\n")
						print("6.Estadísticas de pago\n")
						print("7.Estadísticas de clases\n")
						print("8.Información administrador\n")
						print("9.Regresar\n")	


						opai = int (input("Selecciona una acción: "))

					

						if opai == 1:

							contador = 0
							while True:
								
								numero_vuelos = int (input("\nIngresa el número máximo de vuelos disponibles: ")) 
								print ("----------------------------------")
								print ("Número de vuelos disponibles = {0}".format(numero_vuelos))

								print ("----------------------------------")

								conf = input("¿Desea corregir el número de vuelos que estarán disponibles? S/N: ")

							
								if conf == "S":
								 	
								 	pass

								elif conf == "N":

									break

								else:
									print ("-----------------")
									print ("Opción incorrecta")
									print ("---- ------------") 
									sleep(1)
									os.system("cls")

						elif opai ==2:

							

							vuelodicc = {}

							for x in range (0,numero_vuelos):

								contador +=1

								if contador < numero_vuelos+1:
									
									print("------Ingresar nuevo Vuelo -------\n\n")

									destino = input(" Destino: ")
									hrsalida = input("\nHora de salida: ")
									hrllegada = input ("\nHora de llegada: ")
									costo_viaje_turista = int(input ("\nCosto de viaje Turista: "))
									costo_viaje_negocios = int(input ("\nCosto de viaje Negocios: "))
									costo_viaje_primera_clase = int(input("\nCosto de viaje Primera Clase: "))
									lugares_dis_clase_turista = int(input("\nLugares disponibles clase Turista: "))
									lugares_dis_clase_negocios = int(input("\nLugares disponibles clase Negocios: "))
									lugares_dis_primera_clase = int(input("\nLugares disponibles Primera clase: "))
									fecha_salida_dia = int(input("\nDía de salida (dd): "))
									fecha_salida_mes = input("\nMes de salida (mm): ")
									fecha_salida_año = int(input("\nAño de salida (aaaa): "))

									print ("\nFecha de salida: {0} de {1} de {2}".format(fecha_salida_dia, fecha_salida_mes, fecha_salida_año))

									
									vuelodicc ['vuelo'+str(contador)]=[destino, hrsalida, hrllegada, costo_viaje_turista, costo_viaje_negocios, costo_viaje_primera_clase, lugares_dis_clase_turista, lugares_dis_clase_negocios, lugares_dis_primera_clase, fecha_salida_dia, fecha_salida_mes, fecha_salida_año] 
									
									no_de_vuelo = contador
									

									print("\n---------------------------------")
									print("Vuelo {0} registrado satisfactoriamente".format(no_de_vuelo))
									print("-----------------------------------")

								else:

									print ("----------------------------------------------------------------------------")
									print ("Se ha alcanzado el número máximo de vuelos disponibles por el momento.\nSi desea ingresar un nuevo vuelo, primero deberá eliminar uno existente.")
									print ("---- -----------------------------------------------------------------------") 
									sleep(4)
									os.system("cls")
								

						elif opai ==3:

							
							for x in range(1,len(vuelodicc)+1):

								elemento = vuelodicc.get('vuelo'+str(x))
								
								print("----------------------------------------------")
								print("Vuelo no. {0}".format(x))
								print("Destino: {0}".format(elemento[0]))
								print("Hora Salida: {0}".format(elemento[1]))
								print("Hora Llegada: {0}".format(elemento[2]))
								print("Costo de viaje Turista: {0}".format(elemento[3]))
								print("Costo de viaje Negocios: {0}".format(elemento[4]))
								print("Costo de viaje Primera Clase: {0}".format(elemento[5]))
								print("Lugares disponibles clase Turista: {0}".format(elemento[6]))
								print("Lugares disponibles clase Negocios: {0}".format(elemento[7]))
								print("Lugares disponibles Primera clase: {0}".format(elemento[8]))
								print("Fecha de salida: {0} de {1} de {2}".format(elemento[9],elemento[10],elemento[11]))
								print("----------------------------------------------")

							if len(vuelodicc) == 0:
								print()
								print("-----------------------------")
								print("No existen vuelos disponibles")	
								print("-----------------------------")

						elif opai ==4:

						
							vuelo_a_eliminar = int(input("Ingresa el número de vuelo que quieras eliminar: "))
							del vuelodicc['vuelo'+str(vuelo_a_eliminar)]

							print("--------------------------------------")
							print("Vuelo {0} cancelado satisfactoriamente".format(vuelo_a_eliminar))
							print("--------------------------------------")

							#Corregir (Si se elimina primero un vuelo menor a la cantidad total de vuelos al querer mostrar la lista ya no se muestra)

						elif opai ==5:

							print("\n------ Modificar vuelo ------\n\n")

							print ("1. Destino")
							print ("\n2. Hora de salida")
							print ("\n3. Hora de llegada")
							print ("\n4. Costo de viaje Turista")
							print ("\n5. Costo de viaje Negocios")
							print ("\n6. Costo de viaje Primera Clase")
							print ("\n7. Lugares disponibles clase Turista")
							print ("\n8. Lugares disponibles clase Negocios")
							print ("\n9. Lugares disponibles Primera clase")
							print ("\n10. Día de salida")
							print ("\n11. Mes de salida")
							print ("\n12. Año de salida")

							opmv= int(input("\nSelecciona el dato que deseas modificar: "))

							vuelo_a_modificar=int(input("¿\nQué número de vuelo es el que deseas modificar? "))

							modificando = vuelodicc.get('vuelo'+str(vuelo_a_modificar))
							
							if opmv == 1:
								modificando[opmv-1]=input("Nuevo destino: ")

							elif opmv == 2:
								modificando[opmv-1]=input("Nueva hora de salida: ")

							elif opmv == 3:
								modificando[opmv-1]=input("Nueva hora de llegada: ")

							elif opmv == 4:
								modificando[opmv-1]=int(input("Nuevo costo de viaje Turista: "))

							elif opmv == 5:
								modificando[opmv-1]=int(input("Nuevo costo de viaje Negocios: "))

							elif opmv == 6:
								modificando[opmv-1]=int(input("Nuevo costo de viaje Primera clase: "))

							elif opmv == 7:
								modificando[opmv-1]=int(input("Nuevos lugares disponibles clase Turista: "))

							elif opmv == 8:
								modificando[opmv-1]=int(input("Nuevos lugares disponibles clase Negocios: "))

							elif opmv == 9:
								modificando[opmv-1]=int(input("Nuevos lugares disponibles Primera clase: "))

							elif opmv == 10:
								modificando[opmv-1]=int(input("Nuevo día de salida (dd): "))

							elif opmv == 11:
								modificando[opmv-1]=input("Nuevo mes de salida (mm): ")

							elif opmv == 12:
								modificando[opmv-1]=int(input("Nuevo año de salida (aaaa): "))

							else:
								print ("-----------------")
								print ("Opción incorrecta")
								print ("---- ------------") 
								sleep(1)
								os.system("cls")
							continue

						elif opai ==6:

							while True:

								print("\n------ Estadísticas de Pago ------\n\n")
								print ("1. Efectivo total en cajas")
								print ("\n2. Saldo de pagos por tarjeta")
								print ("\n3. Saldo total de ventas")
								print ("\n4. Número de pagos realizados en efectivo")
								print ("\n5. Número de pagos realizados con tarjeta")
								print ("\n6. Regresar")

								opep= int(input("Selecciona el dato a visualizar: "))


								if opep == 1:

									print("El efectivo total en cajas es: ")

								elif opep == 2:

									print("El saldo de pagos por tarjeta es: ")

								elif opep == 3:

									print("El saldo total de ventas es: ")

								elif opep == 4:

									print("El número de pagos realizados en efectivo es: {0}".format(contadorefectivo))

								elif opep == 5:

									print("El número de pagos realizados con tarjeta es: {0}".format(contadortarjeta))

								elif opep == 6:

									break

								else:
									print ("-----------------")
									print ("Opción incorrecta")
									print ("---- ------------") 
									sleep(1)
									os.system("cls")

							

						elif opai ==7:

							while True:

								print("\n------ Estadísticas de Clase ------\n\n")
								print ("1. Boletos vendidos de la Clase Turista")
								print ("\n2. Boletos vendidos de la clase Negocios")
								print ("\n3. Boletos vendidos de Primera Clase")
								print ("\n4. Clase con mayor número de ventas")
								print ("\n5. Regresar")
								

								opec= int(input("Selecciona el dato a visualizar: "))

								if opec == 1:

									print("La cantidad de boletos vendidos en clase Turista es: {0} ".format(contadorturista))

								elif opec == 2:

									print("La cantidad de boletos vendidos en clase Negocios es: {0} ".format(contadornegocio))

								elif opec == 3:

									print("La cantidad de boletos vendidos en Primera clase es: {0}".format(contadorprimeraclase))

								elif opec == 4:

									if contadorturista > contadornegocio and contadorturista > contadorprimeraclase:
										print("La clase con mayor número de ventas es: clase turista")

									elif contadornegocio > contadorturista and contadornegocio > contadorprimeraclase:
										print("La clase con mayor número de ventas es: clase negocio")

									elif contadorprimeraclase > contadornegocio and contadorprimeraclase > contadorturista:
										print("La clase con mayor número de ventas es: primera clase")

									else:
										break

								elif opec == 5:

									break

								else:
									print ("-----------------")
									print ("Opción incorrecta")
									print ("---- ------------") 
									sleep(1)
									os.system("cls")
						
						elif opai ==8:

							while True: 

								if nombre_a == nombre_ao1:
								
									print("Administrador: {0} {1}".format(nombre_ao1,apellido_ao1))

									print("Sueldo: $35,000")



								elif nombre_a == nombre_ao2:
									print("Administrador: {0} {1}".format(nombre_ao2,apellido_ao2))

									print("Sueldo: $35,000")


								s = input("¿Desea salir? S/N: " )	

								if s == "S":

									break

								elif s == "N":

									pass
							
						elif opai ==9:
							
							break

					
						else:
							print ("-----------------")
							print ("Opción incorrecta")
							print ("---- ------------") 
							sleep(1)
							os.system("cls")
					


				elif ((nombre_a != nombre_ao1 or contraseña_a != contraseña_ao1) or (nombre_a != nombre_ao2 or contraseña_a != contraseña_ao2)):
				
					print ("-------------------------------")
					print ("Contraseña o usuario incorrecto")
					print ("-------------------------------")
					sleep(1)
					os.system('cls')
				



			elif opa == 2:

				break


			else: 
				print ("-----------------")
				print ("Opción incorrecta")
				print ("---- ------------") 
				sleep(1)
				os.system("cls")
		


	elif op ==2:

		while True:

			print("\n------ Cliente ------\n\n")


			print("1.Ingresar")
			print("2.Registrarse")
			print("3.Regresar")

			opc = int(input("Selecciona una opción: "))

			if opc == 1:
				
				usuarioc = input("Usuario: ")
				contraseñac = input ("Contraseña: ")

				for i in range(len(clientes)):
					
					if cliente.usuario == usuarioc and cliente.contraseña ==contraseñac:

						while True:

							print("\n------ Bienvenido {0} ------".format(usuarioc))

							print("\n1. Ver vuelos disponibles.")
							print("\n2. Comprar vuelos.")
							print("\n3. Ver mi información.")
							print("\n4. Regresar.")

							opcu = int(input("Seleciona una opción: "))

					
							if opcu == 1:

								for x in range(len(vuelodicc)):

									elemento = vuelodicc.get('vuelo'+str(x))
									
									print("\nVuelo no. {0}".format(x))
									print("Destino: {0}".format(elemento[0]))
									print("Hora Salida: {0}".format(elemento[1]))
									print("Hora Llegada: {0}".format(elemento[2]))
									print("Costo de viaje Turista: {0}".format(elemento[3]))
									print("Costo de viaje Negocios: {0}".format(elemento[4]))
									print("Costo de viaje Primera Clase: {0}".format(elemento[5]))
									print("Lugares disponibles clase Turista: {0}".format(elemento[6]))
									print("Lugares disponibles clase Negocios: {0}".format(elemento[7]))
									print("Lugares disponibles Primera clase: {0}".format(elemento[8]))
									print("Fecha de salida: {0} de {1} de {2}".format(elemento[9],elemento[10],elemento[11]))
							
							elif opcu == 2:

								print("\n------ Comprar boletos de vuelo ------\n\n")

								num_vuelo = int(input("Ingrese el número de vuelo: "))
								num_boletos = int(input("\nNúmero de boletos: "))

								print("Clase: ")

								print("\n\t1. Turista")
								print("\n\t2. Negocios")
								print("\n\t3. Primera Clase")

								clase_es = int (input("\nSelecciona una clase: "))


								if clase_es == 1:
									contadorturista = contadorturista + 1

								elif clase_es == 2:
									contadornegocio = contadornegocio + 1

								elif clase_es == 3:
									contadorprimeraclase = contadorprimeraclase + 1

								print("\nForma de pago: ")

								print("\n\t1. Tarjeta de crédito o débito")
								print("\n\t2. Efectivo")

								for_pago = int (input("\nSelecciona una forma de pago: "))

								if for_pago == 1:
									contadortarjeta = contadortarjeta + 1

								elif for_pago == 2:
									contadorefectivo = contadorefectivo + 1

								print("\n---------------------------------")
								print("Compra registrada satisfactoriamente")
								print("-----------------------------------")

								compras = []
								compra=Compra(num_vuelo,num_boletos,clase_es,for_pago)
								compras.append(compra)


							elif opcu == 3:

								print("\nCliente: {0} {1}".format(nombrec, apellidoc))

								print("\nEdad: {0}".format(edadc))

								print("\nUsuario: {0}".format(usuarioc))


							elif opcu == 4:

								break

							else:
								print ("-----------------")
								print ("Opción incorrecta")
								print ("---- ------------") 
								sleep(1)
								os.system("cls")

					elif ((usuarioc != cliente.usuario or contraseñac != cliente.contraseña)):
				
						print ("-------------------------------")
						print ("Contraseña o usuario incorrecto")
						print ("-------------------------------")
						sleep(1)
						os.system('cls')
					

			elif opc == 2:
				
				print("\n------ Cliente ------\n\n")

				nombrec = input("Nombre: ")
				apellidoc = input("\nApellido: ")
				edadc = input("\nEdad: ")
				usuarioc = input("\nUsuario: ")
				contraseña = input("\nContraseña: ")
				print("\n-----------------------------------------------")
				print(" {0} {1} ha sido registrado satisfactoriamente.".format(nombrec,apellidoc))
				print("-----------------------------------------------")

				clientes = []
				cliente=Cliente(nombrec,apellidoc,edadc,usuarioc,contraseña)
				clientes.append(cliente)


			elif opc == 3:
				break

			else:
				print ("-----------------")
				print ("Opción incorrecta")
				print ("---- ------------") 
				sleep(1)
				os.system("cls")

	elif op ==3:
		print("--------------------------")
		print("Gracias por su preferencia")
		print("--------------------------")
		sleep(1)
		os.system('cls')
		break

	else:
		print ("-----------------")
		print ("Opción incorrecta")
		print ("---- ------------") 
		sleep(1)
		os.system("cls")


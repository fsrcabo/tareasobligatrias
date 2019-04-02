# En este programa se creará una calculadora

#Zona importaciones

import os
#zona definición de variables y diccionario
selec=1
bucledowhilefalso=0
diccionario={'Suma':'n1+n2', 'Resta':'n1-n2', 'Multiplicación':'n1*n2', 'Division':'n1/n2', 'Exponencial':'n1^n2'}


#Zona de definición e implementación de funciones

#Esta función nos mostrará un menú para que el usuario pueda elegir la opción que quiera.
def menu():
	
	print("Introduzca una opcion de las siguientes: ")
	print("\tOpcion 1.- Suma de dos numeros.")
	print("\tOpcion 2.- Resta de dos numeros.")
	print("\tOpcion 3.- Multiplicación de dos numeros.")
	print("\tOpcion 4.- División de dos numeros.")
	print("\tOpcion 5.- Exponencial de dos numeros,.")
	print("\tOpcion 6.- Salir de el programa.")
	opcion=int(input("Introduzca la opcion elegida: "))
	os.system('cls')

	return opcion
#Funcion que realiza la suma
def Suma():
	n1=pedirnumero1()
	n2=pedirnumero2()
	print("El resultado de la suma es: ",n1+n2)
	os.system('pause')
	os.system('cls')

#Funcion que realiza la resta

def Resta():
	n1=pedirnumero1()
	n2=pedirnumero2()
	print("El resultado de la resta es: ",n1-n2)
	os.system('pause')
	os.system('cls')

#Funcion que realiza la Multiplicacion

def Multip():
	n1=pedirnumero1()
	n2=pedirnumero2()
	
	try:

		resultado=n1*n2
	except IOError:

		print("Hay un error IOError")
	else:

		print("El resultado de la Multiplicación es: ",resultado)

	os.system('pause')
	os.system('cls')

#Funcion que realiza la division

def Division():
	n1=pedirnumero1()
	n2=pedirnumero2()
	try:

		resultado=n1/n2
	except ZeroDivisionError:

		print("¡división por cero!")
	else:

		print("El resultado de la Division es: ",resultado)

	os.system('pause')
	os.system('cls')

#Funcion que realiza ecuacion exponencial

def Exponencial():
	n1=pedirnumero1()
	n2=pedirnumero2()
	print("El resultado de la ecuacion Exponencial es: ",n1**n2)
	os.system('pause')
	os.system('cls')


#pide el primer numero al usuario
def pedirnumero1():

	numero1=int(input("Introduzca un primer numero: "))
	os.system('cls')
	
	return numero1

#pide el segundo numero al usuario
def pedirnumero2():

	numero2=int(input("Introduzca un segundo numero: "))
	os.system('cls')
	
	return numero2


#Cuerpo del programa principal

os.system('cls')
print("Las diferentes operaciones que la calculadora puede realizar son: ")
print (diccionario)
print("\n\n")
os.system('pause')

while(bucledowhilefalso == 0 and selec != 6):
	os.system('cls')
	selec=menu()  	

	if (selec==1):

		Suma()

	elif (selec==2):
	
		Resta()

	elif (selec==3):

		Multip()

	elif (selec==4):

		Division()

	elif (selec==5):

		Exponencial()

	else :

		print("Saliendo del programa")


#Ejercicio 1 

MAYOR_EDAD = 21
#pedimos al usuario que ingrese su edad
edad = input ("Por favor, ingrese su edad: ") 
edad = int(edad)
#si tiene 21 años o mas se imprimira que es mayor de edad
# de lo contrario se imprime que es menor
if edad >= MAYOR_EDAD:
    print ("Es mayor de edad")
else:
    print ("Usted es menor de edad")

#Ejercicio 2

NOTA_APROBADO = 6
#pedimos al usuario que ingrese su nota
nota = input("Ingrese la nota obtenida: ")
nota = int(nota)
#si la nota es igual o mayor a 6 se mostrara arobado
#de lo contrario el mensaje sera desaprobado
if nota >= NOTA_APROBADO:
    print ("Aprobado")
else: print ("Desaprobado")    

#Ejercicio 3
#pedimos al usuario para determinar si es par o impar
numero_ingresado = input ("Por favor ingrese un número: ")
numero_ingresado = int (numero_ingresado)

if (numero_ingresado % 2) == 0:
    print ("Ha ingresado un número par")
else :
    print ("Por favor, ingrese un número par")

#Ejercicio 4
#pedimos al usuario que ingrese su edad
edad = input ("Por favor ingrese su edad: ")
edad = int (edad)
if edad < 12:
#Menor de 12 años es niño
    print ("Niño/a")
elif edad >=12 and edad <18:
#mayor o igual que 12 años y menor que 18 años es adolecente
    print ("Adolescente")
elif edad >=18 and edad <30:
#mayor o igual que 18 años y menor que 30 años es adulto/a joven
    print ("Adulto/a joven")
else:
    #mayor o igual que 30 años adulto/a
    print ("Adulto/a")

#Ejercicio 5
#pedimos al usuario que ingrese una contraseña
contraseña = input ("Por favor ingrese una contraseña: ")
longitud = len (contraseña)
#definimos si la contraseña posee entre 8 y 14 caracteres sera correcta 
#de lo contrario se le pedira ingresar una contraseña valida
if longitud >=8 and longitud <=14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
#importar las funciones
import statistics
import random
#crear la lista de numeros aleatorios
numeros_aleatorios= [random.randint(1,100) for i in range (50)]
print (f"La lista de numeros aleatorios es: {numeros_aleatorios}")

#calculamos la media,mediana y moda

media=statistics.mean (numeros_aleatorios)
mediana=statistics.median (numeros_aleatorios)
moda=statistics.mode (numeros_aleatorios)

print (f"Media: {media}")
print (f"Mediana: {mediana}")
print (f"Moda: {moda}")

#comparamos resultados para determinar el sesgo
if media > mediana and mediana > moda:
    print ("Sesgo positivo o a la derecha: la media > mediana > moda.")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo o a la izquierda: la media < mediana < moda.")
elif media == mediana and mediana == moda:
    print ("Sin sesgo: la media, la mediana y la moda son iguales o muy similares.")
    
#Ejercicio 7
#pedimos al usuario una frase
frase = input ("Por favor, ingrese una frase o palabra: ")
#si la frase posee vocal al final se mostrara la palabra o frase ingresada mas el signo !
#de lo contrario solo se imprimira palabra o frase ingresada
if frase [-1].lower () in "aeiou":
    print (frase + "!")
else:
    print (frase)

#Ejercicio 8
#Pedimos al usuario que ingrese su nombre
nombre = input ("Por favor ingrese su nombre: ")

#pedimos al usuario que ingrese opcion deseada
print ("Elija una opción: ")
print ("1.Mostrar su nombre en mayúsculas.")
print ("2.Mostrar su nombre en minúsculas.")
print ("3.Mostrar su nombre con la primera letra en mayúscula.")
opcion = input ("Ingrese el numero de la opcion (1, 2 o 3): ")

#procesamos la opcion deseada y mostramos el resultado
if opcion == "1":
    nombre_mayuscula = nombre.upper()
    print ("Su nombre es: ", nombre_mayuscula)
elif opcion == "2":
    nombre_minuscula = nombre.lower()
    print ("Su nombre es: ", nombre_minuscula)
elif opcion == "3":
    nombre_iniciado_mayus = nombre.title()
    print ("Su nombre es: ", nombre_iniciado_mayus)
else:
    print ("Opcion ingresada no valida, por favor ingresa 1, 2 o 3.")

#Ejercicio 9
#Pedimos al usuario que ingrese un valor para determinar la magnitud de un terremoto
magnitud_terremoto = float (input ("Por favor ingrese la magnitud del terremoto: "))

#Clasificar la magnitud en la escala de Ritcher y mostramos por pantalla 
if magnitud_terremoto < 3:
    #magnitud menor que 3 "Muy leve" (imperceptible).
    print ("Terremoto muy leve (imperceprtible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    #magnitud mayor o igual 3 y menor que 4 "Leve" (ligeramente perceptible)
    print ("Terremoto leve (ligeramente percetible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    #magnitud mayor o igual que 4 y menor que 5 "Moderado" 
    #(sentido por personas, pero generalmente no causa daños)
    print ("Terremoto moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    #Mayor o igual que 5 y menor que 6 "Fuerte" 
    #(puede causar daños en estructuras débiles)
    print ("Terremoto Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    #Mayor o igual que 6 y menor que 7 Muy Fuerte 
    #(puede causar daños significativos)
    print ("Terremoto muy fuerte (puede causar daños significativos)")
else: #magnitud Mayor o igual que 7 
      #Extremo (puede causar graves daños a gran escala).
      print ("Terremoto extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
# solicita al usuario el hemisferio donde se encuentra
hemisferio = input("¿En que hemisferio te encuentras? (N/S): ").upper()

# validamos la entrada del hemisferio
if hemisferio not in ["N", "S"]:
    print("hemisferio invalido. Por favor ingresa 'N' para Norte o 'S' para Sur")
else:
    # solicitamos mes y dia
    try:
        mes= int(input("Ingresa el numero del mes actual (1-12): "))
        dia= int(input("Ingresa el dia actual: "))

        # validamos el mes y dia ingresado
        if not (1 <= mes <= 12 and 1 <= dia <= 31):
            print("fecha no valida")
        else:
            estacion = ""

            # determinamos la estacion
            if hemisferio == "N":
                # hemisferio Norte
                if (mes == 3 and dia >=21) or (mes > 3 and mes <= 5) or (mes == 6 and dia < 21):
                    estacion = "Primavera"
                elif (mes == 6 and dia >=21) or (mes > 6 and mes <= 8) or (mes == 9 and dia < 21):
                    estacion = "Verano"
                elif (mes == 9 and dia >= 21) or (mes > 9 and mes <= 11) or (mes == 12 and dia < 21):
                    estacion = "Otoño"
                else:
                    estacion = "Invierno"
            else: # hemisferio == "S"
                if (mes == 3 and dia >= 21) or (mes > 6 and mes <= 8) or (mes == 9 and dia < 21):
                    estacion = "Otoño"
                elif (mes == 6 and dia >= 21) or (mes > 6 and mes <= 8) or (mes == 9 and dia < 21):
                    estacion = "Invierno"
                elif (mes == 9 and dia >= 21) or (mes > 9 and mes <= 11) or (mes == 12 and dia < 21):
                    estacion = "Primavera"
                else: # cubre de diciembre 21 a marzo 20
                    estacion = "Verano"

            print(f"Te encuentras en la estacion: {estacion}")
    except ValueError:
            print("entrada no valida. Por favor ingresa numeros para el mes y el dia")

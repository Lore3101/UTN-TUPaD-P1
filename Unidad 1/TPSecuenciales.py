#TODO EL TRABAJO PRACTICO REALIZADO

#1) 
print ("Hola mundo!") 

#2)
#pide al usuario que ingrese su nombre 
nombre = input ("Por favor ingrese su nombre: ")
print(F"Hola, {nombre}!")

#3)
nombre = input ("Por favor ingresa tu nombre")
apellido = input ("Por favor ingresa tu apellido")
edad= input ("¿Que edad tienes?")
residencia = input ("¿Donde vives (lugar de residencia)?")
print (F"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4)
import math
#pedir al usuario el radio del circulo. lo convertimos a numero.
radio = float (input ("Por favor ingresa el radio del circulo: "))
#calculamos el área 
area = math.pi * radio **2
#calculamos el perimetro 
perimetro = 2 * math.pi * radio
#imprimir los resultados
print (f"el area del circulo es:  {area:.2f}")
print (f"el perimetro del circulo es: {perimetro:.2f}")

#5)
#convertir segundos a hs
segundos = int (input ("introduce la cantidad de segundos: "))
# 1 hora = 3600 segundos
horas = segundos /3600
print (f"{segundos} segundos equivalen a {horas:.2f} horas.")

#6)
#tabla de multiplicar
numero = int (input ("Por favor introduce un numero para ver su tabla de multiplicar"))
print (f"\n Tabla de multiplicar del {numero} ")
for i in range (1, 11):
    resultado = numero * i
print (f"{numero} x {i} = {resultado}")

#7)
#calculadora
num1 = int (input ("introduce el primer numero (entero y distinto a 0)"))
num2 = int (input ("introduce el segundo numero (entero y distinto a 0)"))
#validar que los numeros no sea 0
if num1 == 0 or num2 == 0:
    print ("Error: los numeros no pueden ser 0")
#realizamos las operaciones
suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
division = num1/num2
#resultados
print(f"\n Resultados de las operaciones ")
print (f"suma: {num1} + {num2} = {suma}")
print (f"Resta: {num1} - {num2} = {resta}")
print (f"multiplicacion: {num1} * {num2} = {multiplicacion}")
print (f"Division: {num1} / {num2} = {division: .2f}")

#8)
#imc
peso = float (input ("Introduce tu peso en kg (Ejemplo: 55.7): "))
altura = float (input ("Ingresa tu altura en metros (Ejemplo: 1.55): "))
#calculamos el IMC
#IMC= peso / (altura*altura)
imc= peso / (altura**2)
print (f"\nTu indice de Masa Corporal (IMC) es: {imc: .2f}")

#9)
#celsius a fahrenheit
#pedimos la temperatura al usuario
celsius = float (input ("Introduce la temperatura en grados Celsius: "))
#convertimos usando la formula dada 
fahrenheit= (9/5) * celsius +32
print (f"{celsius} °C equivale a {fahrenheit: .2f} °F")

#10)
#calcular promedio
#pedimos al usuario 3 numeros para calcular el promedio
num1 = float (input ("Introduce el primer numero: "))
num2 = float (input("Introduce el segundo numero: "))
num3 = float (input ("Introduce el tercer numero: "))
#calculamos el promedio
promedio = (num1+num2+num3) /3
print (f"\n El promedio de los numeros es: {promedio: .2f}")

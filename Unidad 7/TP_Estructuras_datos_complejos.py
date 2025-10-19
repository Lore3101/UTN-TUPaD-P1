#1)Agregar frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2) Actualizar precios

# Continuando el diccionario del punto 1
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)


#3) Lista solo con las frutas (sin precios)

# Continuando el diccionario del punto 2
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)

#4) Agenda telefónica (cargar 5 y consultar)

# Inicializar un diccionario vacío para los contactos
agenda_telefonica = {}
NUM_CONTACTOS = 5

# Cargar 5 contactos
print(f"Carga de {NUM_CONTACTOS} contactos:")
for i in range(NUM_CONTACTOS):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    agenda_telefonica[nombre] = numero

# Consultar un número
nombre_consulta = input("\nIngrese el nombre del contacto a consultar: ")

# Mostrar el número si existe
if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es: {agenda_telefonica[nombre_consulta]}")
else:
    print(f"El contacto '{nombre_consulta}' no se encuentra en la agenda.")

# Ejemplo de resultado (si los contactos son: {"Juan": "123456", "Ana": "987654", ...} y se consulta "Juan") [cite: 32]
# El número de Juan es: 123456

#5) Palabras únicas y conteo por palabra

frase = input("Ingrese una frase: ")

# Convertir la frase a minúsculas y dividirla en palabras
# Esto facilita el conteo ignorando mayúsculas/minúsculas
palabras = frase.lower().split()

# 1. Palabras únicas (usando un set)
palabras_unicas = set(palabras)

# 2. Diccionario de recuento (contador de frecuencia)
recuento_palabras = {}
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementa su valor; si no, la inicializa en 1
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

# Imprimir resultados
print("\nSalida:")
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento_palabras}")



#6) Promedio de 3 alumnos con tuplas de 3 notas

alumnos = {}
for i in range(3):
    nombre = input(f"Nombre del alumno #{i+1}: ").strip()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")


#7) Sets de aprobados (Parcial 1 y 2)


# Sets de ejemplo de estudiantes que aprobaron cada parcial
# Cada número representa un identificador único de estudiante.
parcial1 = {101, 102, 105, 107, 110} # Aprobados Parcial 1
parcial2 = {102, 103, 105, 108, 110} # Aprobados Parcial 2

print(f"Aprobados Parcial 1: {parcial1}")
print(f"Aprobados Parcial 2: {parcial2}")

# Mostrar los que aprobaron AMBOS parciales (Intersección)
# Se usa el operador '&'
ambos_parciales = parcial1 & parcial2
print(f"\n1. Estudiantes que aprobaron AMBOS parciales (Intersección): {ambos_parciales}")

# Mostrar los que aprobaron SOLO UNO de los dos (Diferencia Simétrica)
# Se usa el operador '^'
solo_uno = parcial1 ^ parcial2
print(f"2. Estudiantes que aprobaron SOLO UNO de los dos (Diferencia Simétrica): {solo_uno}")

# Mostrar la lista total de estudiantes que aprobaron AL MENOS UN parcial (Unión)
# Se usa el operador '|'
al_menos_uno = parcial1 | parcial2
print(f"3. Lista total de estudiantes que aprobaron AL MENOS UNO (Unión): {al_menos_uno}")





#8) Stock por producto (consultar / sumar / agregar)

stock_productos = {"Leche": 50, "Pan": 100, "Huevos": 30}

def gestionar_inventario():
    """Permite al usuario gestionar el inventario mediante un menú."""
    inventario = stock_productos # Usamos el diccionario inicial

    while True:
        print("\n--- Gestión de Inventario ---")
        print(f"Stock actual: {inventario}")
        print("Opciones:")
        print("  (C) - Consultar stock de producto")
        print("  (A) - Agregar unidades o nuevo producto")
        print("  (S) - Salir")
        
        # Usamos .strip() para limpiar espacios y .upper() para hacer la entrada insensible a mayúsculas
        opcion = input("Ingrese una opción: ").strip().upper() 
        
        if opcion == 'C':
            # --- Consultar Stock ---
            producto = input("Ingrese el nombre del producto a consultar: ").strip().capitalize()
            if producto in inventario:
                print(f"✅ El stock de {producto} es: {inventario[producto]} unidades.")
            else:
                print(f"❌ El producto '{producto}' no existe en el inventario.")

        elif opcion == 'A':
            # --- Agregar Unidades / Nuevo Producto ---
            producto = input("Ingrese el nombre del producto a actualizar/agregar: ").strip().capitalize()
            try:
                unidades = int(input("Ingrese la cantidad de unidades a agregar (positiva): "))
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero.")
                continue # Volver al inicio del bucle

            if producto in inventario:
                # Agregar unidades al stock si el producto ya existe
                inventario[producto] += unidades
                print(f"📦 Se agregaron {unidades} unidades. Nuevo stock de {producto}: {inventario[producto]}")
            else:
                # Agregar un nuevo producto si no existe
                inventario[producto] = unidades
                print(f"🆕 Nuevo producto '{producto}' agregado con stock inicial de {unidades}.")

        elif opcion == 'S':
            # --- Salir ---
            print("Saliendo de la gestión de inventario. ¡Hasta luego!")
            break
            
        else:
            print("⚠️ Opción no válida. Por favor, intente de nuevo.")


gestionar_inventario()


#9) Agenda con claves (día, hora) → evento

agenda = {
    ("Lunes", "09:00"): "Reunión scrum",
    ("Martes", "14:30"): "Laboratorio",
    ("Viernes", "18:00"): "Gimnasio"
}

dia = input("Día a consultar (ej. Lunes): ").strip().title()
hora = input("Hora a consultar (HH:MM): ").strip()

clave = (dia, hora)
if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad programada en ese día y hora.")


#10) Invertir país→capital a capital→país


original = {
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago", 
    "Perú": "Lima", 
    "Colombia": "Bogotá"
}

print(f"Diccionario Original (País: Capital):\n{original}")


invertido = {capital: pais for pais, capital in original.items()}

print(f"\nDiccionario Invertido (Capital: País):\n{invertido}")
print("-" * 40)



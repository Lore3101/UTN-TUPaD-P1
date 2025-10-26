"""
practica_archivos.py
-------------------------------------------------------
Resuelve la práctica "Archivos" (Programación I).

Funcionalidades:
1) Crear archivo inicial (si no existe).
2) Leer y mostrar productos desde productos.txt.
3) Agregar productos por teclado (sin borrar los existentes en memoria).
4) Cargar productos en una lista de diccionarios.
5) Buscar producto por nombre (case-insensitive).
6) Guardar productos actualizados sobrescribiendo productos.txt.

Formato del archivo:
nombre,precio,cantidad
Ejemplo:
Lapicera,120.5,30
Cuaderno,450.0,15
Regla,80.0,20
-------------------------------------------------------
"""

from pathlib import Path

ARCHIVO = "productos.txt"


# ---------- Utilidades de conversión y validación ----------

def _to_float(texto: str) -> float:
    """Convierte a float con mensaje claro si falla."""
    try:
        return float(texto)
    except ValueError:
        raise ValueError("El precio debe ser numérico (ej: 199.99).")


def _to_int(texto: str) -> int:
    """Convierte a int con mensaje claro si falla."""
    try:
        return int(texto)
    except ValueError:
        raise ValueError("La cantidad debe ser un entero (ej: 10).")


# ---------- Punto 1/2/4: Carga desde archivo a lista de diccionarios ----------

def cargar_desde_archivo(ruta: str) -> list[dict]:
    """
    Lee productos.txt y devuelve una lista de dicts:
    [{'nombre': str, 'precio': float, 'cantidad': int}, ...]
    Ignora líneas vacías y valida campos.
    """
    productos: list[dict] = []
    path = Path(ruta)

    if not path.exists():
        # Punto 1: Crear archivo inicial si no existe.
        path.write_text(
            "Lapicera,120.5,30\nCuaderno,450.0,15\nRegla,80.0,20\n",
            encoding="utf-8"
        )

    with open(path, "r", encoding="utf-8") as f:
        for nro, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) != 3:
                print(f"Advertencia: línea {nro} inválida -> '{linea}' (se omite)")
                continue

            nombre, precio_txt, cant_txt = [p.strip() for p in partes]
            try:
                producto = {
                    "nombre": nombre,
                    "precio": _to_float(precio_txt),
                    "cantidad": _to_int(cant_txt),
                }
            except ValueError as e:
                print(f"Advertencia: línea {nro} inválida: {e} (se omite)")
                continue

            productos.append(producto)

    return productos


# ---------- Punto 2: Mostrar productos ----------

def mostrar(productos: list[dict]) -> None:
    """Muestra los productos en el formato requerido."""
    if not productos:
        print("No hay productos cargados.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


# ---------- Punto 3: Agregar producto desde teclado ----------

def agregar_desde_teclado(productos: list[dict]) -> None:
    """Solicita datos por teclado y agrega a la lista en memoria."""
    print("\nIngreso de nuevo producto (deje vacío el nombre para cancelar)")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Operación cancelada.")
        return

    precio_txt = input("Precio: ").strip()
    cantidad_txt = input("Cantidad: ").strip()

    try:
        nuevo = {
            "nombre": nombre,
            "precio": _to_float(precio_txt),
            "cantidad": _to_int(cantidad_txt),
        }
    except ValueError as e:
        print(f"Error: {e}")
        return

    productos.append(nuevo)
    print("✅ Producto agregado en memoria. (No se guarda en archivo hasta elegir 'Guardar cambios')")


# ---------- Punto 5: Buscar producto por nombre ----------

def buscar_por_nombre(productos: list[dict]) -> None:
    buscado = input("Ingrese el nombre a buscar: ").strip()
    if not buscado:
        print("Búsqueda cancelada.")
        return

    for p in productos:
        if p["nombre"].lower() == buscado.lower():
            print(f"Encontrado -> Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            return

    print("❌ Producto no encontrado.")


# ---------- Punto 6: Guardar productos (sobrescribir archivo) ----------

def guardar_en_archivo(ruta: str, productos: list[dict]) -> None:
    """
    Sobrescribe productos.txt con el contenido de la lista 'productos'.
    """
    with open(ruta, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print(f"💾 Cambios guardados en '{ruta}'.")


# ---------- Menú interactivo para probar fácilmente todos los puntos ----------

def menu():
    productos = cargar_desde_archivo(ARCHIVO)

    while True:
        print("\n=== Gestión de Productos ===")
        print("1) Mostrar productos (leer y formatear)")
        print("2) Agregar producto (desde teclado)")
        print("3) Buscar producto por nombre")
        print("4) Guardar cambios (sobrescribe productos.txt)")
        print("5) Recargar desde archivo (descarta cambios no guardados)")
        print("0) Salir")
        op = input("Opción: ").strip()

        if op == "1":
            mostrar(productos)
        elif op == "2":
            agregar_desde_teclado(productos)
        elif op == "3":
            buscar_por_nombre(productos)
        elif op == "4":
            guardar_en_archivo(ARCHIVO, productos)
        elif op == "5":
            productos = cargar_desde_archivo(ARCHIVO)
            print("🔄 Archivo recargado.")
        elif op == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()

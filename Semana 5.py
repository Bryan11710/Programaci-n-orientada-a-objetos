# Programa: Registro de Futbolistas del Real Madrid
# Descripción: Este programa permite gestionar un registro de futbolistas del Real Madrid.
# Funcionalidades:
# 1. Agregar un futbolista con su nombre, posición, número de camiseta y estado (activo/inactivo).
# 2. Ver la lista de futbolistas registrados.
# 3. Buscar un futbolista por su nombre.
# Tipos de datos utilizados: string, integer, boolean.

# Diccionario para almacenar los datos de los futbolistas
registro_futbolistas = {}

def agregar_futbolista():
    """
    Función para agregar un futbolista al registro.
    """
    nombre = input("Ingrese el nombre del futbolista: ")
    posicion = input("Ingrese la posición del futbolista (Ej: Delantero, Defensa, Portero): ")
    numero_camiseta = int(input("Ingrese el número de camiseta del futbolista: "))
    estado = input("¿El futbolista está activo? (sí/no): ").strip().lower() == "sí"
    
    registro_futbolistas[nombre] = {
        "posición": posicion,
        "número": numero_camiseta,
        "estado": estado
    }
    print(f"Futbolista '{nombre}' agregado con éxito.\n")

def ver_futbolistas():
    """
    Función para mostrar todos los futbolistas registrados.
    """
    if not registro_futbolistas:
        print("No hay futbolistas registrados.\n")
        return
    
    print("Lista de futbolistas del Real Madrid:")
    for nombre, datos in registro_futbolistas.items():
        estado = "Activo" if datos["estado"] else "Inactivo"
        print(f"Nombre: {nombre}, Posición: {datos['posición']}, Número: {datos['número']}, Estado: {estado}")
    print()

def buscar_futbolista():
    """
    Función para buscar un futbolista por su nombre.
    """
    nombre = input("Ingrese el nombre del futbolista a buscar: ")
    futbolista = registro_futbolistas.get(nombre)
    if futbolista:
        estado = "Activo" if futbolista["estado"] else "Inactivo"
        print(f"Nombre: {nombre}, Posición: {futbolista['posición']}, Número: {futbolista['número']}, Estado: {estado}\n")
    else:
        print(f"El futbolista '{nombre}' no está registrado.\n")

def menu_principal():
    """
    Función principal para mostrar el menú del programa.
    """
    while True:
        print("Menú - Registro de Futbolistas del Real Madrid:")
        print("1. Agregar Futbolista")
        print("2. Ver Futbolistas")
        print("3. Buscar Futbolista")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_futbolista()
        elif opcion == "2":
            ver_futbolistas()
        elif opcion == "3":
            buscar_futbolista()
        elif opcion == "4":
            print("¡Hasta luego, Hala Madrid!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Iniciar el programa
menu_principal()

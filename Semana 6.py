# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad    # Atributo privado (encapsulación)

    def obtener_edad(self):
        # Método para acceder al atributo privado
        return self.__edad

    def hacer_sonido(self):
        # Método que será sobrescrito en las clases derivadas
        raise NotImplementedError("Este método debe ser sobrescrito por una clase derivada")

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza

    def hacer_sonido(self):
        # Sobrescritura del método de la clase base
        return f"{self.nombre} dice: ¡Guau!"

# Clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        # Sobrescritura del método de la clase base
        return f"{self.nombre} dice: ¡Miau!"

# Polimorfismo con múltiples argumentos
def mostrar_sonido(animal):
    print(animal.hacer_sonido())

# Crear instancias de las clases
perro = Perro("Rex", 3, "Pastor Alemán")
gato = Gato("Whiskers", 2, "Blanco")

# Demostración de encapsulación
print(f"La edad de {perro.nombre} es {perro.obtener_edad()} años.")
print(f"La edad de {gato.nombre} es {gato.obtener_edad()} años.")

# Demostración de polimorfismo
mostrar_sonido(perro)
mostrar_sonido(gato)

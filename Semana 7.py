class Persona:
    def __init__(self, nombre, edad):
        """Constructor para inicializar el nombre y la edad."""
        self.nombre = nombre
        self.edad = edad
        print(f"Persona {self.nombre} creada.")

    def saludar(self):
        """Método para saludar."""
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        """Destructor para limpiar recursos."""
        print(f"Persona {self.nombre} eliminada.")


persona1 = Persona("Juan", 25)
persona1.saludar()


del persona1
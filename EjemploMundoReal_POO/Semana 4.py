# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return f"Se vendieron {cantidad} unidades de {self.nombre}."
        else:
            return "Stock insuficiente."


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda.")

    def mostrar_productos(self):
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(producto.mostrar_informacion())


# Ejecución
if __name__ == "__main__":
    tienda = Tienda("Tienda Local")

    # Crear productos
    producto1 = Producto("Manzanas", 0.50, 100)
    producto2 = Producto("Leche", 1.20, 50)

    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    # Mostrar productos
    tienda.mostrar_productos()

    # Realizar venta
    print(producto1.vender(10))
    print(producto1.vender(150))  # Intento de vender más del stock disponible

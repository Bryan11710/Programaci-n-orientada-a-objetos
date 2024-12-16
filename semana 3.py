class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana (7 días):")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            print("No hay temperaturas ingresadas.")
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio de temperaturas de la semana es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()

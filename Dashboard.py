import os
import subprocess
from colorama import init, Fore

init(autoreset=True)

class Dashboard:
    def __init__(self):
        self.ruta_base = os.path.abspath(os.path.dirname(__file__))
        self.unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}
    
    def mostrar_menu(self):
        while True:
            print(Fore.CYAN + "\nMenu Principal - Dashboard")
            for key, value in self.unidades.items():
                print(f"{key} - {value}")
            print("0 - Salir")
            eleccion = input(Fore.YELLOW + "Elige una opción: ").strip()
            if eleccion == '0':
                print(Fore.RED + "Saliendo...")
                break
            elif eleccion in self.unidades:
                self.mostrar_sub_menu(os.path.join(self.ruta_base, self.unidades[eleccion]))
            else:
                print(Fore.RED + "Opción no válida.")

    def mostrar_sub_menu(self, ruta_unidad):
        if not os.path.exists(ruta_unidad):
            print(Fore.RED + "Unidad no encontrada.")
            return
        
        sub_carpetas = sorted([f.name for f in os.scandir(ruta_unidad) if f.is_dir()])
        while True:
            print(Fore.GREEN + "\nSubmenú - Selecciona una subcarpeta")
            for i, carpeta in enumerate(sub_carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Regresar")
            
            eleccion = input(Fore.YELLOW + "Elige una opción: ").strip()
            if eleccion == '0':
                break
            elif eleccion.isdigit() and 1 <= int(eleccion) <= len(sub_carpetas):
                self.mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[int(eleccion)-1]))
            else:
                print(Fore.RED + "Opción no válida.")
    
    def mostrar_scripts(self, ruta_sub_carpeta):
        if not os.path.exists(ruta_sub_carpeta):
            print(Fore.RED + "Carpeta no encontrada.")
            return
        
        scripts = sorted([f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')])
        while True:
            print(Fore.BLUE + "\nScripts disponibles:")
            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar")
            
            eleccion = input(Fore.YELLOW + "Elige un script para ver o ejecutar: ").strip()
            if eleccion == '0':
                break
            elif eleccion.isdigit() and 1 <= int(eleccion) <= len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[int(eleccion)-1])
                self.mostrar_codigo(ruta_script)
            else:
                print(Fore.RED + "Opción no válida.")

    def mostrar_codigo(self, ruta_script):
        try:
            with open(ruta_script, 'r', encoding='utf-8') as archivo:
                codigo = archivo.read()
                print(Fore.MAGENTA + f"\n--- Código de {ruta_script} ---\n{codigo}")
                if input(Fore.YELLOW + "¿Ejecutar script? (1: Sí, 0: No): ").strip() == '1':
                    self.ejecutar_codigo(ruta_script)
        except FileNotFoundError:
            print(Fore.RED + "El archivo no se encontró.")

    def ejecutar_codigo(self, ruta_script):
        try:
            subprocess.run(['python', ruta_script], check=True)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error al ejecutar el código: {e}")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")

if __name__ == "__main__":
    Dashboard().mostrar_menu()


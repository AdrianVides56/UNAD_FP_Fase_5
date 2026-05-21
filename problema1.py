# Adrian Felipe Vides Jimenez
# Grupo 16
# Ingenieria Electronica - UNAD
# Codigo Fuente: autoría propia

from enum import Enum
import secrets
import string


# Clase que contiene datos del cliente
class Cliente:
    def __init__(self,duracion, clics):
        self.ID = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))  # Asigna un ID único al cliente
        self.duracion = duracion
        self.clics = clics
        self.clasificacion = None  # Inicialmente sin clasificación de compromiso

# Estructura para las clasificaciones de compromiso
class ClasificacionCompromiso(Enum):
    ALTO = "Alto"
    MEDIO = "Medio"
    BAJO = "Bajo"

# Funcion para registrar un nuevo cliente
def crear_cliente():
    nuevo_cliente = Cliente(0, 0)

    # Pedir al usuario que ingrese la duración y los clics del cliente
    nuevo_cliente.duracion = ingresar_duracion()
    nuevo_cliente.clics = ingresar_clics()
    return nuevo_cliente

# Fucion para validar la entrada de clics del cliente
def ingresar_clics():
    while True:
        try:
            clics = int(input("Ingrese el número de clics del cliente: "))
            if clics < 0:
                print('\033[91m' + "El número de clics no puede ser negativo. Intente nuevamente." + '\033[0m')
                continue
            return clics
        except (ValueError, EOFError, KeyboardInterrupt):
            print('\033[91m' + "Entrada inválida. Por favor, ingrese un número entero." + '\033[0m')

# Funcion para validar la entrada de duracion de la sesion del cliente
def ingresar_duracion():
    while True:
        try:
            duracion = int(input("Ingrese la duración de la sesión del cliente (en segundos): "))
            if duracion <= 0:
                print('\033[91m' + "La duración no puede ser cero o negativa. Intente nuevamente." +'\033[0m')
                continue
            return duracion
        except (ValueError, EOFError, KeyboardInterrupt):
            print('\033[91m' + "Entrada inválida. Por favor, ingrese un número entero." + '\033[0m')


# Funcion para calcular la clasificacion de compromiso de un cliente
def calcular_compromiso(cliente):
    if cliente.duracion > 180 and cliente.clics > 8:
        return ClasificacionCompromiso.ALTO
    elif cliente.duracion < 60 or cliente.clics < 3:
        return ClasificacionCompromiso.BAJO
    else:
        return ClasificacionCompromiso.MEDIO


# Funcion para clasificar a los clientes segun su compromiso
def clasificar_clientes(clientes):
    if not clientes:
        print('\033[91m' + "No hay clientes para clasificar." + '\033[0m')
        return []
    for cliente in clientes:
        clasificar_cliente(cliente)
    return clientes


def clasificar_cliente(cliente):
    clasificacion = calcular_compromiso(cliente)
    cliente.clasificacion = clasificacion
    return cliente


# Funcion para imprimir la clasificacion de los clientes en una tabla
def imprimir_resultados(clientes):
    if not clientes:
        print('\033[91m' + "No hay clientes para mostrar." + '\033[0m')
        return

    encabezado_id = "ID del cliente"
    encabezado_clas = "Clasificación"
    ancho_id = max(len(encabezado_id), max(len(cliente.ID) for cliente in clientes))
    ancho_clas = max(len(encabezado_clas), max(len(cliente.clasificacion.value) for cliente in clientes))

    print(f"┌{'─'*(ancho_id + 2)}┬{'─'*(ancho_clas + 2)}┐")
    print(f"│ {encabezado_id:<{ancho_id}} │ {encabezado_clas:<{ancho_clas}} │")
    print(f"├{'─'*(ancho_id + 2)}┼{'─'*(ancho_clas + 2)}┤")
    for cliente in clientes:
        print(f"│ {cliente.ID:<{ancho_id}} │ {cliente.clasificacion.value:<{ancho_clas}} │")
    print(f"└{'─'*(ancho_id + 2)}┴{'─'*(ancho_clas + 2)}┘")

# Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print('\033[1m' + "\nSeleccione una opción:" + '\033[0m')
    print('\033[1m' + "1." + '\033[0m' + " Ver resultados")
    print('\033[1m' + "2." + '\033[0m' + " Agregar nuevo cliente")
    print('\033[1m' + "3." + '\033[0m' + " Salir")
    print("")


if __name__ == "__main__":
    # Matriz de clientes con sus respectivas duraciones y clics
    # Estos datos son de ejemplo
    datos_clientes = [
        Cliente(200, 10),
        Cliente(20, 2),
        Cliente(100, 5),
        Cliente(50, 1),
        Cliente(300, 15),
        Cliente(150, 7)
    ]

    clasificar_clientes(datos_clientes)  # Clasificar los clientes iniciales antes de mostrar el menú

    print('\033[1m' + "\n Programa de clasificación de clientes según su compromiso" + '\033[0m')

    while True:
        mostrar_menu()
        try:
            opcion = input("Ingrese el número de la opción deseada: ")
            if opcion == '1':
                imprimir_resultados(datos_clientes)
            elif opcion == '2':
                nuevo_cliente = crear_cliente()
                clasificar_cliente(nuevo_cliente)  # Clasificar el nuevo cliente antes de agregarlo a los resultados
                datos_clientes.append(nuevo_cliente)
                print('\033[92m' + "Nuevo cliente agregado y clasificado." + '\033[0m')
            elif opcion == '3':
                print('\033[93m' + "Saliendo del programa" + '\033[0m')
                break
            else:
                print('\033[91m' + "Opción inválida. Por favor, seleccione una opción válida." + '\033[0m')
        except (EOFError, KeyboardInterrupt): # Maneja la interrupción del programa (Ctrl+C o Ctrl+D)
            break

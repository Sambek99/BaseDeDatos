from tabulate import tabulate
from colorama import init, Fore, Style

init(autoreset=True)

def mostrar_menu_principal():
    print(Fore.RED + Style.BRIGHT + "BIENVENIDO A LA CIUDADELA\n")
    menu = [
        ["1", "MODO VISITANTE"],
        ["2", "MODO PROPIETARIO"],
        ["3", "MODO ADMINISTRADOR"],
        ["4", "SALIR"]
    ]
    print(tabulate(menu, headers=["Opción", "Descripción"], tablefmt="grid"))
    
def menu_visitante():
    print(Fore.YELLOW + "Modo Visitante: Elija la tabla que como desea ingresar")
    menu = [
        ["1", "ANUNCIARSE MEDIANTE EL GUARDIA"],
        ["2", "CÓDIGO QR"]
    ]
    print(tabulate(menu, headers=["Opción", "Tabla"], tablefmt="grid"))

def menu_propietario():
    print(Fore.BLUE + "Modo Propietario: Elija la tabla que desea consultar")
    menu = [
        ["1", "CASA"],
        ["2", "CÓDIGO QR"],
        ["3", "LISTA NEGRA"],
        ["4", "PROPIETARIOS EN MORA"],
        ["5", "PAGOS PENDIENTES"],
        ["6", "GENERAR QR"],
        ["7", "GENERAR AUTORIZACION"],
        ["8", "AGREGAR LISTA NEGRA"]
    ]
    print(tabulate(menu, headers=["Opción", "Tabla"], tablefmt="grid"))

def menu_administrador():
    print(Fore.MAGENTA + "Modo Administrador: Elija la tabla que desea consultar")
    menu = [
        ["1", "REGISTRAR PAGOS PROPIETARIOS"],
        ["2", "MOSTRAR TODAS LAS CASAS"],
        ["3", "MOSTRAR VEHÍCULOS Y SUS RESIDENTES"]
    ]
    print(tabulate(menu, headers=["Opción", "Tabla"], tablefmt="grid"))

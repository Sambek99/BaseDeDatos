import os
import pymysql
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import init, Fore, Style

load_dotenv()
init(autoreset=True)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

connection = pymysql.connect(
    host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME
)
cur = connection.cursor()

def mostrar_tabla(query, headers):
    try:
        cur.execute(query)
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        else:
            print(Fore.YELLOW + "No se encontraron resultados.")
    except Exception as e:
        print(Fore.RED + f"Error al ejecutar la consulta: {e}")

def mostrar_menu_principal():
    print(Fore.RED + Style.BRIGHT + "BIENVENIDO A LA CIUDADELA\n")
    menu = [
        ["1", "MODO VISITANTE"],
        ["2", "MODO PROPIETARIO"],
        ["3", "MODO GUARDIA"],
        ["4", "SALIR"]
    ]
    print(tabulate(menu, headers=["Opción", "Descripción"], tablefmt="grid"))

def menu_visitante():
    print(Fore.YELLOW + "Modo Visitante: Elija la tabla que desea consultar")
    menu = [
        ["1", "VISITANTE"],
        ["2", "CÓDIGO QR"],
        ["3", "GUARDIA"],
        ["4", "VISITANTES AUTORIZADOS"]
    ]
    print(tabulate(menu, headers=["Opción", "Tabla"], tablefmt="grid"))

def menu_propietario():
    print(Fore.BLUE + "Modo Propietario: Elija la tabla que desea consultar")
    menu = [
        ["1", "CASA"],
        ["2", "CÓDIGO QR"],
        ["3", "LISTA NEGRA"],
        ["4", "PROPIETARIOS EN MORA"],
        ["5", "PAGOS PENDIENTES"]
    ]
    print(tabulate(menu, headers=["Opción", "Tabla"], tablefmt="grid"))

def menu_guardia():
    print(Fore.LIGHTBLUE_EX + "Modo Guardia: Elija la tabla que desea consultar")
    menu = [
        ["1", "PRE AUTORIZAR"],
        ["2", "CASA"],
        ["3", "VEHÍCULOS Y RESIDENTES"]
    ]
    print(tabulate(menu, headers=["Opción", "Tabla"], tablefmt="grid"))

valido = True
while valido:
    clear()
    mostrar_menu_principal()
    try:
        op = int(input(Fore.GREEN + "Escoja una opción: "))
        if op == 1:  # Modo Visitante
            clear()
            menu_visitante()
            opv = int(input("Escoja una opción: "))
            if opv == 1:
                mostrar_tabla("SELECT * FROM visitante LIMIT 10;", ["Número de cédula", "Nombre", "Apellido"])
            elif opv == 2:
                mostrar_tabla("SELECT * FROM codigoqr LIMIT 10;", ["ID", "Código"])
            elif opv == 3:
                mostrar_tabla("SELECT numero_de_cedula, correo, nombre, apellido, telefono FROM guardia LIMIT 10;", ["Número de cédula", "Correo", "Nombre", "Apellido", "Teléfono"])
            elif opv == 4:
                mostrar_tabla("SELECT v.nombre, v.apellido, ag.cedula_guardia, ag.hora, ag.fecha FROM autorizacionguardia ag JOIN visitante v ON ag.cedula_visitante = v.numero_de_cedula WHERE ag.fecha = '2024-03-03';", ["Nombre", "Apellido", "Cédula Guardia", "Hora", "Fecha"])
        elif op == 2:  # Modo Propietario
            clear()
            menu_propietario()
            opr = int(input("Escoja una opción: "))
            if opr == 1:
                mostrar_tabla("SELECT codigo_catastral, numero_de_cedula, villa, manzana, telefono1 FROM casa LIMIT 10;", ["Código Catastral", "Número de cédula", "Villa", "Manzana", "Teléfono"])
            elif opr == 2:
                mostrar_tabla("SELECT * FROM codigoqr LIMIT 10;", ["ID", "Código"])
            elif opr == 3:
                mostrar_tabla("SELECT * FROM lista_negra LIMIT 10;", ["Número de cédula", "Código Catastral"])
            elif opr == 4:
                mostrar_tabla("SELECT p.nombre, p.apellido, p.numero_de_cedula, c.codigo_catastral, c.villa, c.manzana FROM propietario p JOIN casa c ON p.numero_de_cedula = c.numero_de_cedula WHERE p.en_mora = TRUE;", ["Nombre", "Apellido", "Cédula", "Código Catastral", "Villa", "Manzana"])
            elif opr == 5:
                mostrar_tabla("SELECT p.nombre, p.apellido, p.numero_de_cedula, COUNT(pa.id_pago) AS pagos_realizados FROM propietario p LEFT JOIN pagos pa ON p.numero_de_cedula = pa.cedula_propietario WHERE YEAR(pa.fecha_pago) = 2024 GROUP BY p.numero_de_cedula HAVING pagos_realizados < 12;", ["Nombre", "Apellido", "Cédula", "Pagos Realizados"])
        elif op == 3:  # Modo Guardia
            clear()
            menu_guardia()
            opg = int(input("Escoja una opción: "))
            if opg == 1:
                mostrar_tabla("SELECT * FROM preautorizacion LIMIT 10;", ["ID", "Fecha", "Estado"])
            elif opg == 2:
                mostrar_tabla("SELECT codigo_catastral, numero_de_cedula, villa, manzana, telefono1 FROM casa LIMIT 10;", ["Código Catastral", "Número de cédula", "Villa", "Manzana", "Teléfono"])
            elif opg == 3:
                mostrar_tabla("SELECT v.placa, v.modelo, v.color, c.villa, c.manzana, p.nombre as propietario, GROUP_CONCAT(r.nombre) as residentes FROM vehiculo v JOIN casa c ON v.codigo_catastral = c.codigo_catastral JOIN propietario p ON c.numero_de_cedula = p.numero_de_cedula LEFT JOIN residente r ON c.codigo_catastral = r.codigo_catastral GROUP BY v.placa ORDER BY c.villa;", ["Placa", "Modelo", "Color", "Villa", "Manzana", "Propietario", "Residentes"])
        elif op == 4:  # Salir
            print(Fore.CYAN + "Gracias por utilizar el sistema. ¡Hasta pronto!")
            valido = False
        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")
        input(" ")
    except ValueError:
        print(Fore.RED + "Por favor, ingrese un número válido.")
    except Exception as e:
        print(Fore.RED + f"Error inesperado: {e}")

connection.close()
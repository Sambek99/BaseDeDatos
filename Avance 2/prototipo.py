import os
import pymysql
from dotenv import load_dotenv
from tabulate import tabulate
from colorama import init, Fore, Style
import pymysql
import qrcode
from io import BytesIO
from PIL import Image
from datetime import datetime, timedelta


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

def obtener_datos_en_lista(query, headers):
    try:
        cur.execute(query)
        rows = cur.fetchall()
        if rows:
            #print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
            return [list(row) for row in rows]  # Convertir cada fila a lista y devolver como lista de listas
        else:
            print(Fore.YELLOW + "No se encontraron resultados.")
            return []
    except Exception as e:
        print(Fore.RED + f"Error al ejecutar la consulta: {e}")
        return []

def ejecutar_query(query):
    try:
        cur.execute(query)
        connection.commit()  # Confirmar los cambios si es un query de escritura
        print(Fore.GREEN + "Proceso exitoso.")
    except Exception as e:
        print(Fore.RED + f"No se realizó la operación: {e}")


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
        ["5", "PAGOS PENDIENTES"],
        ["6", "GENERAR QR"],
        ["7", "GENERAR AUTORIZACION"],
        ["8", "AGREGAR LISTA NEGRA"]
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



def insertar_y_generar_qr(cedula_visitante, cedula, nombre, apellido, fecha_visita):
    try:
        # Llamar al procedimiento almacenado
        cur.callproc('insertar_y_generar_qr', 
                     (cedula_visitante, cedula, nombre, apellido, fecha_visita))
        
        # Confirmar que la transacción se ha realizado
        connection.commit()
        
        print(Fore.GREEN + "El visitante y QR han sido gestionados correctamente.")
    except pymysql.MySQLError as e:
        # En caso de error, hacer rollback para revertir cualquier cambio realizado
        connection.rollback()
        print(Fore.RED + f"Error en el procedimiento almacenado: {e}")


def insertar_black_list(cedula_visitante, codigo_catastral):
    # Query para verificar si el visitante existe
    check_query = "SELECT 1 FROM visitante WHERE numero_de_cedula = '{}'".format(cedula_visitante)
    
    # Query para insertar un nuevo visitante si no existe
    insert_visitante_query = "INSERT INTO visitante VALUES ('{}', '{}', '{}')".format(cedula_visitante,nombre,apellido)
    
    # Query para insertar el código QR generado
    insert_black_list = "INSERT INTO lista_negra (cedula_visitante, codigo_catastral) VALUES ('{}', '{}')".format(cedula_visitante,codigo_catastral)
    
    try:
        # Verificar si el visitante existe
        cur.execute(check_query)
        rows = cur.fetchall()
        print(2323)
        if rows:
            print(Fore.YELLOW + "El visitante ya existe.")

            # Insertar en lista negra
            ejecutar_query(insert_black_list)
            print(Fore.GREEN + "Agregado a la lista negra y almacenado en la base de datos.")
        else:
            # Si no existe, insertamos al visitante
            ejecutar_query(insert_visitante_query)
            print(Fore.GREEN + "Visitante insertado exitosamente.")
            
            # Insertar en lista negra
            ejecutar_query(insert_black_list)
            print(Fore.GREEN + "Agregado a la lista negra y almacenado en la base de datos.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def insertar_y_generar_autorizacion(cedula_guardia, cedula_visitante, cedula_propietario, nombre, apellido, fecha_visita, fecha_fin):
    try:
        # Llamar al procedimiento almacenado
        cur.callproc('insertar_y_generar_autorizacion', 
                     (cedula_guardia, cedula_visitante, cedula_propietario, nombre, apellido, fecha_visita, fecha_fin))
        
        # Confirmar que la transacción se ha realizado
        connection.commit()
        
        print(Fore.GREEN + "Visitante y autorización han sido gestionados correctamente.")
    except pymysql.MySQLError as e:
        # En caso de error, hacer rollback para revertir cualquier cambio realizado
        connection.rollback()
        print(Fore.RED + f"Error en el procedimiento almacenado: {e}")


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
            correo = input(Fore.BLUE + "Ingrese su correo: ")
            conta = input(Fore.BLUE + "Ingrese su Contraseña: ")
            # Aquí se está utilizando .format() para asegurar que los valores estén dentro de comillas.
            query = "SELECT numero_de_cedula FROM propietario WHERE correo = '{}' AND contrasena = '{}'".format(correo, conta)
            cedula = obtener_datos_en_lista(query,["Cedula"])[0][0]
            opr = int(input("Escoja una opción: "))
            if opr == 1:
                mostrar_tabla("SELECT codigo_catastral, numero_de_cedula, villa, manzana, telefono1 FROM casa WHERE numero_de_cedula = '{}';".format(cedula), ["Código Catastral", "Número de cédula", "Villa", "Manzana", "Teléfono"])
            elif opr == 2:
                mostrar_tabla("SELECT * FROM codigoqr WHERE cedula_propietario = '{}';".format(cedula), ["ID", "Código"])
            elif opr == 3:
                mostrar_tabla("SELECT ln.numero_de_cedula, ln.codigo_catastral FROM lista_negra ln JOIN casa c ON ln.codigo_catastral = c.codigo_catastral WHERE c.numero_de_cedula = '{}';".format(cedula), ["Número de cédula", "Código Catastral"])
            elif opr == 4:
                mostrar_tabla("SELECT p.nombre, p.apellido, p.numero_de_cedula, c.codigo_catastral, c.villa, c.manzana FROM propietario p JOIN casa c ON p.numero_de_cedula = c.numero_de_cedula WHERE p.en_mora = TRUE AND p.numero_de_cedula = '{}';".format(cedula), ["Nombre", "Apellido", "Cédula", "Código Catastral", "Villa", "Manzana"])
            elif opr == 5:
                mostrar_tabla("SELECT p.nombre, p.apellido, p.numero_de_cedula, COUNT(pa.fecha_pago) AS pagos_realizados FROM propietario p LEFT JOIN pagos pa ON p.numero_de_cedula = pa.cedula_propietario AND YEAR(pa.fecha_pago) = 2024 WHERE p.numero_de_cedula = '{}' GROUP BY p.numero_de_cedula HAVING pagos_realizados < 12;".format(cedula), ["Nombre", "Apellido", "Cédula", "Pagos Realizados"])
            elif opr == 6:
                cedula_visitante = input(Fore.BLUE + "Ingrese la cedula del visitante: ")
                nombre = input(Fore.BLUE + "Ingrese el nombre del visitante: ")
                apellido = input(Fore.BLUE + "Ingrese el apellido del visitante: ")
                fecha_inicio = input(Fore.BLUE + "Ingrese la fecha de la visita en formato AAAA-MM-DD: ")
                insertar_y_generar_qr(cedula_visitante,cedula,nombre,apellido,fecha_inicio)
            elif opr == 7:
                cedula_guardia= "0901556789"
                cedula_visitante = input(Fore.BLUE + "Ingrese la cedula del visitante: ")
                nombre = input(Fore.BLUE + "Ingrese el nombre del visitante: ")
                apellido = input(Fore.BLUE + "Ingrese el apellido del visitante: ")
                fecha_inicio = input(Fore.BLUE + "Ingrese la fecha de la visita en formato AAAA-MM-DD: ")
                fecha_fin = input(Fore.BLUE + "Ingrese la fecha fin de la visita en formato AAAA-MM-DD: ")
                insertar_y_generar_autorizacion(cedula_guardia,cedula_visitante,cedula,nombre,apellido,fecha_inicio,fecha_fin)
            elif opr == 8:
                codigo_catastral = obtener_datos_en_lista("SELECT codigo_catastral FROM casa WHERE numero_de_cedula = '{}';".format(cedula),["Codigo_catastral"])[0][0]
                cedula_visitante = input(Fore.BLUE + "Ingrese la cedula del visitante: ")
                insertar_black_list(cedula_visitante, codigo_catastral)
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
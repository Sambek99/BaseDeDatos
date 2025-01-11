import os
from datetime import datetime, timedelta
from tabulate import tabulate
from colorama import Fore
from database import execute_query

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_tabla(query, headers, params=None):
    try:
        rows = execute_query(query, params)
        if rows:
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        else:
            print(Fore.YELLOW + "No se encontraron resultados.")
    except Exception as e:
        print(Fore.RED + f"Error al ejecutar la consulta: {e}")

def insertar_y_generar_qr(cedula_visitante, cedula, nombre, apellido, fecha_visita):
    check_query = "SELECT 1 FROM visitante WHERE numero_de_cedula = %s"
    insert_visitante_query = "INSERT INTO visitante (numero_de_cedula, nombre, apellido) VALUES (%s, %s, %s)"
    fecha_fin = (datetime.strptime(fecha_visita, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    insert_query_qr = "INSERT INTO codigoqr (cedula_visitante, cedula_propietario, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)"
    
    try:
        rows = execute_query(check_query, (cedula_visitante,))
        if rows:
            print(Fore.YELLOW + "El visitante ya existe.")
            execute_query(insert_query_qr, (cedula_visitante, cedula, fecha_visita, fecha_fin))
            print(Fore.GREEN + "El QR ha sido generado y almacenado en la base de datos.")
        else:
            execute_query(insert_visitante_query, (cedula_visitante, nombre, apellido))
            print(Fore.GREEN + "Visitante insertado exitosamente.")
            execute_query(insert_query_qr, (cedula_visitante, cedula, fecha_visita, fecha_fin))
            print(Fore.GREEN + "El QR ha sido generado y almacenado en la base de datos.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def insertar_blackl_list(cedula_visitante, nombre, apellido, codigo_catastral):
    check_query = "SELECT 1 FROM visitante WHERE numero_de_cedula = %s"
    insert_visitante_query = "INSERT INTO visitante (numero_de_cedula, nombre, apellido) VALUES (%s, %s, %s)"
    insert_black_list = "INSERT INTO lista_negra (cedula_visitante, codigo_catastral) VALUES (%s, %s)"
    
    try:
        rows = execute_query(check_query, (cedula_visitante, nombre, apellido))
        if rows:
            print(Fore.YELLOW + "El visitante ya existe.")
            execute_query(insert_black_list, (cedula_visitante, codigo_catastral))
            print(Fore.GREEN + "Agregado a la lista negra y almacenado en la base de datos.")
        else:
            execute_query(insert_visitante_query, (cedula_visitante, nombre, apellido))
            print(Fore.GREEN + "Visitante insertado exitosamente.")
            execute_query(insert_black_list, (cedula_visitante, codigo_catastral))
            print(Fore.GREEN + "Agregado a la lista negra y almacenado en la base de datos.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def insertar_y_generar_autorizacion(cedula_guardia, cedula_visitante, cedula_propietario, nombre, apellido, fecha_visita, fecha_fin):
    check_query = "SELECT 1 FROM visitante WHERE numero_de_cedula = %s"
    insert_visitante_query = "INSERT INTO visitante (numero_de_cedula, nombre, apellido) VALUES (%s, %s, %s)"
    insert_query_at = "INSERT INTO preautorizacion (cedula_guardia, cedula_visitante, cedula_propietario, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s)"
    
    try:
        rows = execute_query(check_query, (cedula_visitante,))
        if rows:
            print(Fore.YELLOW + "El visitante ya existe.")
            execute_query(insert_query_at, (cedula_guardia, cedula_visitante, cedula_propietario, fecha_visita, fecha_fin))
            print(Fore.GREEN + "La autorizacion ha sido generada y almacenada en la base de datos.")
        else:
            execute_query(insert_visitante_query, (cedula_visitante, nombre, apellido))
            print(Fore.GREEN + "Visitante insertado exitosamente.")
            execute_query(insert_query_at, (cedula_guardia, cedula_visitante, cedula_propietario, fecha_visita, fecha_fin))
            print(Fore.GREEN + "La autorizacion ha sido generada y almacenada en la base de datos.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
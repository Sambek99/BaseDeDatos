import os
from datetime import datetime, timedelta
from tabulate import tabulate
from colorama import Fore
from database import execute_query,execute_stored_procedure

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
    try:
        # Llamar al procedimiento almacenado usando la función del archivo database.py
        params = (cedula_visitante, cedula, nombre, apellido, fecha_visita)
        execute_stored_procedure('insertar_y_generar_qr', params)
        
        print(Fore.GREEN + "El visitante y QR han sido gestionados correctamente.")
    except Exception as e:
        print(Fore.RED + f"Error en el procedimiento almacenado: {e}")


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
    try:
        # Parámetros para el procedimiento almacenado
        params = (cedula_guardia, cedula_visitante, cedula_propietario, nombre, apellido, fecha_visita, fecha_fin)
        
        # Llamar al procedimiento almacenado usando la función del archivo database.py
        execute_stored_procedure('insertar_y_generar_autorizacion', params)
        
        print(Fore.GREEN + "Visitante y autorización han sido gestionados correctamente.")
    except Exception as e:
        print(Fore.RED + f"Error en el procedimiento almacenado: {e}")

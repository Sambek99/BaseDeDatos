import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

def execute_query(query, params=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            connection.commit()
            return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def execute_stored_procedure(proc_name, params=None):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.callproc(proc_name, params)
            connection.commit()
            return cursor.fetchall()  # Devuelve los resultados si es necesario
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

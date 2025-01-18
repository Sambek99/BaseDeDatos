import datetime
from colorama import Fore

from database import execute_query
from menus import mostrar_menu_principal, menu_visitante, menu_propietario, menu_administrador
from utils import clear_screen, mostrar_tabla, insertar_y_generar_qr, insertar_blackl_list, insertar_y_generar_autorizacion

def main():
    valido = True
    while valido:
        clear_screen()
        mostrar_menu_principal()
        try:
            op = int(input(Fore.GREEN + "Escoja una opción: "))
            if op == 1:  # Modo Visitante
                  clear_screen()
                menu_visitante()
                opv = int(input("Escoja una opción: "))
                if opv == 1:
                        cedula_visitante = input(Fore.LIGHTGREEN_EX +"Ingrese su cedula: ")
                        manzana = input(Fore.BLUE + "Ingrese la manzana a la que se dirige: ")
                        villa = input(Fore.BLUE + "Ingrese la villa a la que se dirige: ")
                        print(Fore.RED + "El guardia esta llamando...")
                        pase = rd.randint(0,1)
                        time.sleep(5)
                        if pase == 0:
                            print('Lo lamento no puede ingresar')
                        else:
                            hora= datetime.now().strftime("%H:%M:%S")
                            fecha= datetime.now().strftime('%Y-%m-%d')
                            querycodigo_catastral = "SELECT * FROM casa WHERE manzana = %s AND villa = %s"
                            codigo_catastral = execute_query(querycodigo_catastral, (manzana, villa))
                            query_autorizacionguardia = "INSERT INTO autorizacionguardia (cedula_visitante, codigo_catastral, hora, fecha) VALUES (%s,%s,%s,%s)"
                            execute_query(query_autorizacionguardia,  (cedula_visitante,codigo_catastral,hora,fecha) )
                            print(Fore.GREEN + "Puede ingresar")

                elif opv == 2:
                        codigo_qr = input("Ingrese el id de codigoqr: ")
                        query_codigo_qr = 'SELECT id FROM codigoqr WHERE id = %s'
                        pase = execute_query(query_codigo_qr, codigo_qr)
                        if pase:
                            print(Fore.GREEN + "Puede Ingresar")
                        else:
                            print("Codigo qr invalido")
            elif op == 2:  # Modo Propietario
                clear_screen()
                menu_propietario()
                correo = input(Fore.BLUE + "Ingrese su correo: ")
                conta = input(Fore.BLUE + "Ingrese su Contraseña: ")
                query = "SELECT numero_de_cedula FROM propietario WHERE correo = %s AND contrasena = %s"
                cedula = execute_query(query, (correo, conta))[0][0]
                opr = int(input("Escoja una opción: "))
                if opr == 1:
                    mostrar_tabla("SELECT codigo_catastral, numero_de_cedula, villa, manzana, telefono1 FROM casa WHERE numero_de_cedula = %s;", ["Código Catastral", "Número de cédula", "Villa", "Manzana", "Teléfono"], (cedula,))
                elif opr == 2:
                    mostrar_tabla("SELECT * FROM codigoqr WHERE cedula_propietario = %s;", ["ID", "Código"], (cedula))
                elif opr == 3:
                    mostrar_tabla("SELECT ln.numero_de_cedula, ln.codigo_catastral FROM lista_negra ln JOIN casa c ON ln.codigo_catastral = c.codigo_catastral WHERE c.numero_de_cedula = %s;", ["Número de cédula", "Código Catastral"], (cedula,))
                elif opr == 4:
                    mostrar_tabla("SELECT p.nombre, p.apellido, p.numero_de_cedula, c.codigo_catastral, c.villa, c.manzana FROM propietario p JOIN casa c ON p.numero_de_cedula = c.numero_de_cedula WHERE p.en_mora = TRUE AND p.numero_de_cedula = %s;", ["Nombre", "Apellido", "Cédula", "Código Catastral", "Villa", "Manzana"], (cedula,))
                elif opr == 5:
                    mostrar_tabla("SELECT p.nombre, p.apellido, p.numero_de_cedula, COUNT(pa.fecha_pago) AS pagos_realizados FROM propietario p LEFT JOIN pagos pa ON p.numero_de_cedula = pa.cedula_propietario AND YEAR(pa.fecha_pago) = 2024 WHERE p.numero_de_cedula = %s GROUP BY p.numero_de_cedula HAVING pagos_realizados < 12;", ["Nombre", "Apellido", "Cédula", "Pagos Realizados"], (cedula,))
                elif opr == 6:
                    cedula_visitante = input(Fore.BLUE + "Ingrese la cedula del visitante: ")
                    nombre = input(Fore.BLUE + "Ingrese el nombre del visitante: ")
                    apellido = input(Fore.BLUE + "Ingrese el apellido del visitante: ")
                    fecha_inicio = input(Fore.BLUE + "Ingrese la fecha de la visita en formato AAAA-MM-DD: ")
                    insertar_y_generar_qr(cedula_visitante, cedula, nombre, apellido, fecha_inicio)
                elif opr == 7:
                    cedula_guardia = "0901556789"
                    cedula_visitante = input(Fore.BLUE + "Ingrese la cedula del visitante: ")
                    nombre = input(Fore.BLUE + "Ingrese el nombre del visitante: ")
                    apellido = input(Fore.BLUE + "Ingrese el apellido del visitante: ")
                    fecha_inicio = input(Fore.BLUE + "Ingrese la fecha de la visita en formato AAAA-MM-DD: ")
                    fecha_fin = input(Fore.BLUE + "Ingrese la fecha fin de la visita en formato AAAA-MM-DD: ")
                    insertar_y_generar_autorizacion(cedula_guardia, cedula_visitante, cedula, nombre, apellido, fecha_inicio, fecha_fin)
                elif opr == 8:
                    cedula_guardia = "0901556789"
                    cedula_visitante = input(Fore.BLUE + "Ingrese la cedula del visitante: ")
                    nombre = input(Fore.BLUE + "Ingrese el nombre del visitante: ")
                    apellido = input(Fore.BLUE + "Ingrese el apellido del visitante: ")
                    insertar_blackl_list(cedula_guardia, cedula_visitante, cedula, nombre, apellido)
            elif op == 3:  # Modo Administrador
                clear_screen()
                correo_admin = input(Fore.LIGHTBLUE_EX + "Ingrese su correo: ")
                contra_admin = input(Fore.LIGHTBLUE_EX + "Ingrese su contraseña: ")
                if correo_admin != "admin@gmail.com" or contra_admin != "Contramaster":
                    print(Fore.RED + "\nLo lamento, pero no tiene acceso a esta sección.")
                    print(Fore.RED + "Correo o contraseña incorrectos.")
                    input(" ")
                    continue
                clear_screen()
                menu_administrador()
                opg = int(input("Escoja una opción: "))
                cedula_administrador = "0900000001"
                if opg == 1:
                    cedula_propietario = input(Fore.LIGHTBLUE_EX + "Ingrese la cédula del propietario: ")
                    monto = 55.00
                    fecha_pago = datetime.datetime.now().strftime('%Y-%m-%d')
                    query = "INSERT INTO pagos (cedula_propietario, cedula_administrador, monto, fecha_pago) VALUES (%s, %s, %s, %s)"
                    execute_query(query, (cedula_propietario, cedula_administrador, monto, fecha_pago))
                    print(Fore.GREEN + "Pago registrado exitosamente.")
                    mostrar_tabla("SELECT cedula_propietario, monto, fecha_pago FROM pagos WHERE cedula_propietario = %s;", ["Cédula Propietario", "Monto", "Fecha de Pago"], (cedula_propietario,))
                    
                elif opg == 2:
                    mostrar_tabla("SELECT codigo_catastral, numero_de_cedula, villa, manzana, telefono1 FROM casa;", ["Código Catastral", "Número de cédula", "Villa", "Manzana", "Teléfono"])
                elif opg == 3:
                    mostrar_tabla("SELECT v.placa, v.modelo, v.color, c.villa, c.manzana, p.nombre as propietario, GROUP_CONCAT(r.nombre) as residentes FROM vehiculo v JOIN casa c USING(codigo_catastral) JOIN propietario p USING(numero_de_cedula) LEFT JOIN residente r USING(codigo_catastral) GROUP BY v.placa ORDER BY c.villa;", ["Placa", "Modelo", "Color", "Villa", "Manzana", "Propietario", "Residentes"])
            elif op == 4:  # Salir
                print(Fore.CYAN + "Gracias por utilizar el sistema. ¡Hasta pronto!")
                valido = False
            else:
                print(Fore.RED + "Opción no válida. Intente de nuevo.")
            input(" ")
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número válido.")
            input(" ")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")

if __name__ == "__main__":
    main()

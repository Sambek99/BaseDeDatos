import random as rd
import time
propietarios_dict = {
    "22 15 ": "Juan Pérez",
    "18 10 ": "María González",
    "25 12 ": "Carlos Martínez",
    "30 20 ": "Ana López",
    "40 25 ": "Luis Ramírez",
    "35 18 ": "Sofía Torres",
    "28 14 ": "Miguel Chávez",
    "33 16 ": "Laura Fernández",
    "29 11 ": "Jorge Castro",
    "22 17 ": "Elena Morales"}
valido = True
while valido:
    print("Bienvenido")
    print("Escoja el metodo que desea probar")
    print("1 MODO VISITANTE \n2 MODO PROPIETARIO \n3 MODO GUARDIA")
    op = int(input("Escoja una opción: "))
    while (op not in [1,2,3]):
        op = int(input("Escoja una opción: "))
    if (op == 1):
        print("Bienvenido")
        print("Escoja el metodo que desea probar")
        print("1 PREAUTORIZADO \n2 CÓDIGO QR\n3 SALIR")
        opv = int(input("Escoja una opción: "))
        while (isinstance(opv, int) and opv not in [1,2,3]):
            opv = int(input("Escoja una opción: "))
        if (opv == 1):
            nombre = input("Ingrese su nombre: ")
            cedula = input("Ingrese su cédula: ")
            mz = input("A que manzana se dirige: ")
            villa = input("A que villa se dirige: ")
            autorizado = rd.randint(0,1)
            casa = mz  + " " + villa + " "  
            if casa in propietarios_dict.keys(): 
                if (autorizado == 0):
                    print("LLAMANDO AL PROPIETARIO...")
                    time.sleep(3)
                    w = rd.randint(0,1)
                    if (w == 0):
                        print("EL PROPIETARIO NO CONTESTÓ\nPOR FAVOR INTENTELO MÁS TARDE")
                        valido = False
                    else:
                        print("Bienvenido")
                        valido = False
                else:
                    print(nombre + " ESTA AUTORIZADO\nBIENVENIDO")
                    valido= False
            else:
                print("VILLA NO EXISTE")
                valido = False
print("GRACIAS")
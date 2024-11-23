import random as rd
import time
import datetime as dt
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
visitantes = {
    "0102030405": ["Juan Pérez", "MZ-10", "V-15", "2024-11-22"],
    "0203040506": ["María González", "MZ-5", "V-8", "2024-11-21"],
    "0304050607": ["Carlos Martínez", "MZ-3", "V-20", "2024-11-20"],
    "0405060708": ["Ana López", "MZ-7", "V-14", "2024-11-19"],
    "0506070809": ["Luis Ramírez", "MZ-12", "V-5", "2024-11-18"],
    "0607080910": ["Sofía Torres", "MZ-8", "V-10", "2024-11-17"],
    "0708091011": ["Miguel Chávez", "MZ-9", "V-25", "2024-11-16"],
    "0809101112": ["Laura Fernández", "MZ-4", "V-19", "2024-11-15"],
    "0910111213": ["Jorge Castro", "MZ-6", "V-22", "2024-11-14"],
    "1011121314": ["Elena Morales", "MZ-1", "V-30", "2024-11-13"]
}
preautorizado = {
    "0102030405": ["Juan Pérez", "MZ-10", "V-15", "2024-11-22", "2024-11-24"],
    "0203040506": ["María González", "MZ-5", "V-8", "2024-11-21", "2024-11-23"],
    "0304050607": ["Carlos Martínez", "MZ-3", "V-20", "2024-11-20", "2024-11-22"],
    "0405060708": ["Ana López", "MZ-7", "V-14", "2024-11-19", "2024-11-21"],
    "0506070809": ["Luis Ramírez", "MZ-12", "V-5", "2024-11-18", "2024-11-21"],
    "0607080910": ["Sofía Torres", "MZ-8", "V-10", "2024-11-17", "2024-11-18"],
    "0708091011": ["Miguel Chávez", "MZ-9", "V-25", "2024-11-16", "2024-11-18"],
    "0809101112": ["Laura Fernández", "MZ-4", "V-19", "2024-11-15", "2024-11-18"],
    "0910111213": ["Jorge Castro", "MZ-6", "V-22", "2024-11-14", "2024-11-16"],
    "1011121314": ["Elena Morales", "MZ-1", "V-30", "2024-11-13", "2024-11-15"]
}

lista_negra = {
    "0102030405": "Juan Pérez",
    "0203040506": "María González",
    "0304050607": "Carlos Martínez"
}
valido = True
while valido:
    print("Bienvenido")
    print("Escoja el metodo que desea probar")
    print("1 MODO VISITANTE \n2 MODO PROPIETARIO \n3 MODO GUARDIA")
    op = int(input("Escoja una opción: "))
    while (op not in [1,2,3]):
        op = int(input("Escoja una opción: "))
    if (op == 1):
        print()
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
    elif (op == 2):
        print()
        print("Bienvenido")
        print("Escoja el metodo que desea probar")
        print("1 PRE AUTORIZAR \n2 Historial de ingreso\n3 GENERAR QR \n4 LISTA NEGRA")
        opr = int(input("Escoja una opción: "))
        while (isinstance(opr, int) and opr not in [1,2,3,4]):
            opr = int(input("Escoja una opción: "))
        if (opr == 1):
            nombre = input("Ingrese el nombre: ")
            cedula = input("Ingrese la cédula: ")
            fecha=  input("Ingrese la fecha inicio AAAA/MM/DD: ")
            fechaFin =  input("Ingrese la fecha fin AAAA/MM/DD: ")
            mz = rd.randint(1,25)
            villa = rd.randint(1,29)
            datos  = ["{}".format(nombre), "MZ-{}".format(mz), "V-{}".format(villa), "{}".format(fecha), "{}".format(fechaFin)]
            preautorizado.update({cedula: datos})
            print("SE GENERO LA PREAUTPRIZACION PARA LA PERSONA: {}\n CON FECHAS\n INICIO:{}\nFIN: {}".format(nombre,fecha,fechaFin))
            valido = False
        elif (opr== 2):
            print("HISTORIAL DE VISITAS: ")
            for i in visitantes.keys():
                    print("{}: {}".format(i," ".join(visitantes[i])))
            valido = False
        elif (opr == 3):
            nombre = input("Ingrese el nombre: ")
            cedula = input("Ingrese la cédula: ")
            fecha= dt.datetime.now() 
            dias = input("CUANTOS DIAS DE VALIDEZ: ")
            fechaFin =  fecha + dt.timedelta(days=int(dias))
            qr = hash(nombre+cedula+str(fecha)+str(fechaFin))
            print("SE GENERO EL QR PARA LA PERSONA: {}\nCODIGO: {}".format(nombre,qr))
            valido = False
        elif (opr == 4):
            print("1 MOSTRAR LISTA NEGRA \n2 AGREGAR A LISTA NEGRA")
            opl = int(input("Escoja una opción: "))
            while (isinstance(opl, int) and opl not in [1,2,3,4]):
                opl = int(input("Escoja una opción: "))
            if (opl == 1):
                for i in lista_negra.keys():
                    print("{}: {}".format(i,lista_negra[i]))
            elif (opl == 2):
                nombre = input("Ingrese el nombre: ")
                cedula = input("Ingrese la cédula: ")
                lista_negra.update({cedula:nombre})
                print("SE AGREGO A {} A LA LISTA NEGRA".format(nombre))
            valido = False
    elif (op == 3):
        print()
        print("Bienvenido")
        print("Escoja el metodo que desea probar")
        print("1 PRE AUTORIZAR \n2 BUSCAR PROPIETARIO")
        opg = int(input("Escoja una opción: "))
        while (isinstance(opg, int) and opg not in [1,2,3,4]):
            opg = int(input("Escoja una opción: "))
        if (opg == 1):
            nombre = input("Ingrese el nombre: ")
            cedula = input("Ingrese la cédula: ")
            mz = input("A que manzana se dirige: ")
            villa = input("A que villa se dirige: ")
            casa = mz  + " " + villa
            if cedula not in lista_negra.keys():
                print("SE REGISTRA A {} CON INGRESO A LA CASA {}".format(nombre,casa))
            else: 
                print("PERSONA EN LISTA NEGRA, NEGAR INGRESO")
            valido = False
        elif (opg== 2):
            mz = input("A que manzana se dirige: ")
            villa = input("A que villa se dirige: ")
            casa = mz  + " " + villa + " "  
            if casa in propietarios_dict.keys(): 
                print(casa + "de " + propietarios_dict[casa]+ " Telefono: 0994567310")
            valido = False
print("GRACIAS")
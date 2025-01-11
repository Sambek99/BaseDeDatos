# MANUAL DE USUARIO

## Prerrequisitos
1. **Python**: Asegúrese de tener Python instalado en su sistema.
2. **Dependencias**: Instale los paquetes de Python necesarios utilizando el siguiente comando:
    ```sh
    pip install pymysql python-dotenv tabulate colorama qrcode pillow
    ```
3. **Variables de Entorno**: Cree un archivo `.env` en el directorio raíz con el siguiente contenido:
    ```env
    DB_HOST=your_database_host
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_NAME=your_database_name
    ```

## Estructura de Archivos
- `config.py`: Carga las variables de entorno para la configuración de la base de datos.
- `database.py`: Gestiona las conexiones a la base de datos y la ejecución de consultas.
- `menus.py`: Muestra varios menús para diferentes modos de usuario.
- `utils.py`: Contiene funciones utilitarias para varias operaciones.
- `main.py`: El archivo principal de la aplicación.

## Ejecutar la Aplicación
Para ejecutar la aplicación, ejecute el siguiente comando en su terminal:
```sh
python 'Avance 2/main.py'
```

## Modos de Usuario
La aplicación admite tres modos de usuario: Visitante, Propietario y Administrador. Cada modo proporciona diferentes funcionalidades.

### Menú Principal
Al ejecutar la aplicación, verá el menú principal:
```
BIENVENIDO A LA CIUDADELA

+--------+--------------------+
| Opción | Descripción        |
+--------+--------------------+
| 1      | MODO VISITANTE     |
| 2      | MODO PROPIETARIO   |
| 3      | MODO ADMINISTRADOR |
| 4      | SALIR              |
+--------+--------------------+
```
Seleccione una opción ingresando el número correspondiente.

### Modo Visitante
TODO:

### Modo Propietario
Si selecciona "MODO PROPIETARIO", se le pedirá que ingrese su correo electrónico y contraseña. Después de la autenticación exitosa, verá el siguiente menú:
```
Modo Propietario: Elija la tabla que desea consultar

+--------+----------------------+
| Opción | Tabla                |
+--------+----------------------+
| 1      | CASA                 |
| 2      | CÓDIGO QR            |
| 3      | LISTA NEGRA          |
| 4      | PROPIETARIOS EN MORA |
| 5      | PAGOS PENDIENTES     |
| 6      | GENERAR QR           |
| 7      | GENERAR AUTORIZACION |
| 8      | AGREGAR LISTA NEGRA  |
+--------+----------------------+
```
Seleccione una opción para realizar la acción correspondiente.
Este código es parte de un sistema que permite a un propietario interactuar con una base de datos para consultar y gestionar información relacionada con su propiedad. Aquí se tiene un resumen de lo que hace:

### Menú de opciones: 
Se llama a la función menu_propietario() para mostrar un menú con opciones disponibles para el propietario.
<img src="https://github.com/user-attachments/assets/be883cc4-7cae-4225-980d-3863b95cc333" width="300"/>

### Opciones del menú: 
Según la opción elegida por el usuario (opr):

### Ingreso de credenciales: 
Solicita al usuario que ingrese su correo y contraseña. Utiliza estos datos para formar una consulta SQL que verifica las credenciales en la tabla propietario. Si las credenciales son correctas, obtiene el número de cédula del propietario desde la base de datos usando la función obtener_datos_en_lista.


Opción 1: Muestra información sobre la casa del propietario.

<img src="https://github.com/user-attachments/assets/6ce8d767-5ba6-4ce0-a67d-caa5133d868a" width="500"/>

Opción 2: Muestra los códigos QR asociados al propietario.

<img src="https://github.com/user-attachments/assets/8c38a6ea-feb7-4b34-a0c7-37180d8745fa" width="500"/>

Opción 3: Muestra la lista negra relacionada con las propiedades del propietario.

<img src="https://github.com/user-attachments/assets/3717f2ba-07fb-4607-92fd-28117bfbb255" width="500"/>

Opción 4: Muestra información de propietarios en mora.

Opción 5: Muestra pagos pendientes de los propietarios para el año 2024.

<img src="https://github.com/user-attachments/assets/f0b7fdbf-f773-4be2-9a9c-57ecebafeead" width="500"/>

Opción 6: Permite generar un QR para un visitante, ingresando sus datos.

![image](https://github.com/user-attachments/assets/9f2148b6-1280-4626-bf83-f92a6561123b)

Opción 7: Genera una autorización para un visitante, ingresando su cédula, nombre, apellido y fechas de visita.

![image](https://github.com/user-attachments/assets/8b1e2464-6ed2-4aa8-97e2-b96bc6533c79)

Opción 8: Agrega a un visitante a la lista negra.


### Modo Administrador
Si selecciona "MODO ADMINISTRADOR", se le pedirá que ingrese su correo electrónico y contraseña. 
correo: admin@gmail.com
contraseña: Contramaster

Si la autenticacion falla se mostrara un texto en rojo de que las credenciales fueron invalidas. Después de la autenticación exitosa, verá el siguiente menú:
```
Modo Administrador: Elija la tabla que desea consultar

+--------+------------------------------------+
| Opción | Tabla                              |
+--------+------------------------------------+
| 1      | REGISTRAR PAGOS PROPIETARIOS       |
| 2      | MOSTRAR TODAS LAS CASAS            |
| 3      | MOSTRAR VEHÍCULOS Y SUS RESIDENTES |
+--------+------------------------------------+
```
Seleccione una opción para realizar la acción correspondiente.

## Funciones Utilitarias
La aplicación incluye varias funciones utilitarias para manejar tareas comunes:

- **clear_screen**: Limpia la pantalla del terminal.
- **mostrar_tabla**: Muestra una tabla basada en la consulta y los encabezados proporcionados.
- **insertar_y_generar_qr**: Inserta un visitante y genera un código QR.
- **insertar_blackl_list**: Inserta un visitante en la lista negra.
- **insertar_y_generar_autorizacion**: Inserta un visitante y genera una autorización.

## Manejo de Errores
La aplicación incluye manejo de errores para gestionar excepciones y proporcionar mensajes de error significativos. Si ocurre un error, se mostrará en texto rojo.

## Conclusión
Este manual proporciona una guía completa para ejecutar y utilizar la aplicación. Siga las instrucciones cuidadosamente para asegurar una experiencia fluida. Si encuentra algún problema, consulte los mensajes de error para obtener orientación.

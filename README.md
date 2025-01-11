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

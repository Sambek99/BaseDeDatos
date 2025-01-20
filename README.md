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
Si selecciona "MODO VISITANTE", se le abrira el siguiente menu de opciones:
```
Modo Visitante: Elija la tabla que desea consultar
+--------+----------------------------------+
| Opción | Descripción                      |
+--------+----------------------------------+
| 1      | ANUNCIARSE MEDIANTE EL GUARDIA   |
| 2      | CODIGO QR                        |
+--------+----------------------------------+
Seleccione una opccion para ingresar a la ciudadela
```
Con la opcion "ANUNCIARCE MEDIANTE EL GUARDIA" se le pedira que ingrese su cedula y diga su manzana y villa, posteriormente se llamara a la casa para validad su ingreso.
Con la opcion "Codigo QR" se le pedira que ingrese el codigo y se validara que este vigente.
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

## Views

Este proyecto tiene 4 views, ademas de esto cada una cuenta con un procedure especifico con el pre-fijo obtener y su parametro especifico:

1. **HistorialDePagos**  
   Vista destinada a manejar y mostrar el historial de pagos realizados.
   
**ObtenerHistorialDePagos(cedula_propietario)**

**Parámetro de Entrada:**
- `cedula_propietario` (CHAR(10)): Cédula del propietario del que se quiere ver el historial.
**Funcionamiento:**
    Muestra un historial de pagos de los pagos del propietario ingresado a traves de su numero de cedula  

2. **HistorialPreAutorizados**  
   Vista diseñada para gestionar y presentar el historial de preautorizaciones.

**ObtenerHistorialPreautorizados(cedula_propietario)**

**Parámetro de Entrada:**
- `cedula_propietario` (CHAR(10)): Cédula del propietario del que se quiere ver el historial.
**Funcionamiento:**
    Muestra un historial de los Preautorizados con el nombre del visitante el apellido del mismo y la fecha.
    
3. **HistorialCodigoQR**  
   Vista utilizada para visualizar y trabajar con el historial de códigos QR generados o utilizados.

**ObtenerHistorialCodigoQR(cedula_propietario)**

**Parámetro de Entrada:**
- `cedula_propietario` (CHAR(10)): Cédula del propietario del que se quiere ver el historial.
**Funcionamiento:**
    Muestra un historial de los codigosQR con el nombre del visitante el apellido del mismo y la fecha.
   
4. **ListaNegra**
    Vista utilizada para visualizar y el nombre de las personas en la lista negra con el codigo catastral responsable de que esa persona este ahí.
   
**ObtenerListaNegra(codigo_catastral)**

**Parámetro de Entrada:**
- `codigo_catastral` (CHAR(25)): Codigo de la casa de la que se quiere ver la lista negra.
  **Funcionamiento:**
  Muestra las personas en la lista negra de esa casa.
   


## Manejo de Errores
La aplicación incluye manejo de errores para gestionar excepciones y proporcionar mensajes de error significativos. Si ocurre un error, se mostrará en texto rojo.

## Conclusión
Este manual proporciona una guía completa para ejecutar y utilizar la aplicación. Siga las instrucciones cuidadosamente para asegurar una experiencia fluida. Si encuentra algún problema, consulte los mensajes de error para obtener orientación.


# DESCRIPCIÓN DE CODIGOS SQL


# Stored Procedures para Gestión de Visitantes y Generación de Códigos QR en la Ciudadela

Este repositorio contiene procedimientos almacenados para gestionar el registro de visitantes, la generación de códigos QR y la creación de autorizaciones de acceso en la base de datos `ciudadela`. A continuación, se describen los stored procedures disponibles y su uso.

## Procedimientos Almacenados

### 1. `insertar_y_generar_qr`

Este procedimiento se encarga de verificar si un visitante ya existe en la base de datos y, si no es así, lo registra. Luego, genera un código QR para el visitante, con una validez de un día desde la fecha de la visita.

**Parámetros de Entrada:**
- `cedula_visitante` (CHAR(10)): Cédula del visitante.
- `cedula_propietario` (CHAR(10)): Cédula del propietario que autoriza la visita.
- `nombre` (VARCHAR(50)): Nombre del visitante.
- `apellido` (VARCHAR(50)): Apellido del visitante.
- `fecha_visita` (DATE): Fecha de la visita.

**Funcionamiento:**
1. **Inicio de Transacción:** Se inicia una transacción para asegurar la consistencia de los datos.
2. **Verificación del Visitante:** Se verifica si el visitante ya está registrado. Si no, se inserta un nuevo registro en la tabla `visitante`.
3. **Cálculo de Fecha de Fin:** Se calcula `fecha_fin` como un día después de `fecha_visita`.
4. **Inserción en `codigoqr`:** Se inserta un nuevo registro en la tabla `codigoqr` con los datos del visitante y las fechas de inicio y fin.
5. **Manejo de Errores:** Si ocurre un error, se revierte la transacción.
6. **Confirmación de Transacción:** Si todo es exitoso, se confirma la transacción (COMMIT).

**Ejemplo de Uso:**
```sql
CALL insertar_y_generar_qr('1234567890', '0987654321', 'Juan', 'Pérez', '2025-01-19');
```

### 2. `insertar_y_generar_autorizacion`

Este procedimiento almacenado se utiliza para crear una autorización de acceso para un visitante. La autorización está vinculada al guardia que aprueba la entrada y al propietario que recibe al visitante. 

**Parámetros de Entrada:**
- `cedula_guardia` (CHAR(10)): Cédula del guardia encargado de autorizar la entrada.
- `cedula_visitante` (CHAR(10)): Cédula del visitante que desea ingresar.
- `cedula_propietario` (CHAR(10)): Cédula del propietario que autoriza la visita.
- `nombre` (VARCHAR(50)): Nombre del visitante.
- `apellido` (VARCHAR(50)): Apellido del visitante.
- `fecha_visita` (DATE): Fecha de inicio de la visita.
- `fecha_fin` (DATE): Fecha de fin de la visita.

**Funcionamiento:**
1. **Inicio de Transacción:** Se inicia una transacción para asegurar que todas las operaciones se realicen de manera segura y coherente.
   
2. **Verificación del Visitante:** Se verifica si el visitante ya está registrado en la tabla `visitante`. Si no está registrado, se inserta un nuevo registro con la cédula, nombre y apellido del visitante.
   
3. **Inserción en `preautorizacion`:** Se inserta un nuevo registro en la tabla `preautorizacion` con los datos del guardia, visitante, propietario, y las fechas de inicio y fin de la visita.
   
4. **Manejo de Errores:** Si ocurre un error durante el proceso, se revierte la transacción completa para evitar inconsistencias en la base de datos.

5. **Confirmación de Transacción:** Si todo se ejecuta correctamente, la transacción se confirma (COMMIT), garantizando que los datos se guarden de manera permanente.

**Ejemplo de Uso:**
```sql
CALL insertar_y_generar_autorizacion('1122334455', '1234567890', '0987654321', 'Juan', 'Pérez', '2025-01-19', '2025-01-20');
```

# TRIGGERS EN EL SISTEMA

## 1. Trigger: update_en_mora_on_payment
Este trigger se activa después de insertar un nuevo registro en la tabla `pagos`.

### Funcionamiento:
- Se ejecuta automáticamente después de registrar un nuevo pago
- Actualiza el estado de mora del propietario a FALSE
- Asegura que el estado de mora se actualice inmediatamente después del pago

### ¿Por qué se creó?
- Mantiene la consistencia de datos entre pagos y estado de mora
- Automatiza la actualización del estado del propietario
- Reduce errores humanos en la gestión de estados de mora

## 2. Trigger: validate_guardia_authorization
Este trigger se activa antes de insertar un nuevo registro en la tabla `autorizacionguardia`.

### Funcionamiento:
- Verifica si el visitante está en la lista negra para esa casa específica
- Si el visitante está en la lista negra, impide la inserción
- Lanza un error con mensaje específico si la validación falla

### ¿Por qué se creó?
- Implementa una capa de seguridad adicional
- Previene autorizaciones a visitantes en lista negra
- Automatiza la validación de restricciones de acceso


# PERMISOS DE USUARIOS EN EL SISTEMA

La siguiente tabla muestra los permisos asignados a cada tipo de usuario en el sistema:

| Objeto/Usuario          | Propietario    | Visitante      | Residente | Guardia        | Administrador |
|------------------------ |-------------   |--------------- |-----------|--------------  |---------------|
| propietario             | SELECT, INSERT | -              | -         | -              | ALL           |
| casa                    | SELECT, INSERT | -              | -         | -              | ALL           |
| visitante               | -              | SELECT, INSERT | -         | -              | ALL           |
| lista_negra             | -              | SELECT         | -         | -              | ALL           |
| autorizacionguardia     | -              | -              | -         | SELECT, UPDATE | ALL           |
| codigoqr                | -              | -              | -         | SELECT, INSERT | ALL           |
| HistorialPreAutorizados | SELECT         | -              | -         | -              | ALL           |
| HistorialDePagos        | -              | -              | -         | SELECT         | ALL           |
| insertar_y_generar_qr   | -              | -              | EXECUTE   | -              | ALL           |
| insertar_y_generar_autorizacion| -       | -              | EXECUTE   | -              | ALL           |

**Notas:**
- (-) indica que no tiene permisos sobre ese objeto
- El administrador tiene privilegios completos (ALL) sobre toda la base de datos

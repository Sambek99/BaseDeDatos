CREATE DATABASE ciudadela;
USE ciudadela;

-- Tabla propietario
CREATE TABLE propietario (
    numero_de_cedula CHAR(10) PRIMARY KEY, -- Exactamente 10 caracteres
    correo VARCHAR(320) UNIQUE NOT NULL,  -- Tamaño máximo recomendado por RFC
    contrasena VARCHAR(255) NOT NULL,     -- Hash de contraseñas
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    huella_dactilar VARCHAR(255),         -- Longitud extendida para posibles datos biométricos
    telefono CHAR(10),                    -- Exactamente 10 caracteres
    en_mora BOOLEAN DEFAULT FALSE         -- Valor por defecto
);

-- Tabla casa
CREATE TABLE casa (
	codigo_catastral CHAR(25) PRIMARY KEY, 
    numero_de_cedula CHAR(10) NOT NULL,
    villa TINYINT UNSIGNED,
    manzana TINYINT UNSIGNED,
    telefono1 CHAR(10),
    telefono2 CHAR(10),
    telefono3 CHAR(10),
	FOREIGN KEY (numero_de_cedula) REFERENCES propietario(numero_de_cedula)
);

-- Tabla residente
CREATE TABLE residente (
    numero_de_cedula CHAR(10) PRIMARY KEY, -- Exactamente 10 caracteres
    codigo_catastral CHAR(25) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    telefono CHAR(10),                   -- Exactamente 10 caracteres
    FOREIGN KEY (codigo_catastral) REFERENCES casa(codigo_catastral)
);

-- Tabla visitante
CREATE TABLE visitante (
    numero_de_cedula CHAR(10) PRIMARY KEY, -- Exactamente 10 caracteres
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL
);

-- Tabla vehiculo
CREATE TABLE vehiculo (
    placa CHAR(10) PRIMARY KEY, -- Exactamente 10 caracteres
    codigo_catastral CHAR(25) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    matricula VARCHAR(50) NOT NULL,
	FOREIGN KEY (codigo_catastral) REFERENCES casa(codigo_catastral)
);

-- Tabla lista_negra
CREATE TABLE lista_negra (
    numero_de_cedula CHAR(10),  -- Clave foránea a la tabla visitante
    codigo_catastral CHAR(25),  -- Clave foránea a la tabla casa
    PRIMARY KEY (numero_de_cedula, codigo_catastral),  -- Combinación única de ambas claves
    FOREIGN KEY (numero_de_cedula) REFERENCES visitante(numero_de_cedula),  -- Relación con la tabla visitante
    FOREIGN KEY (codigo_catastral) REFERENCES casa(codigo_catastral)  -- Relación con la tabla casa
);

-- Tabla administrador
CREATE TABLE administrador (
    numero_de_cedula CHAR(10) PRIMARY KEY, -- Exactamente 10 caracteres
    correo VARCHAR(320) UNIQUE NOT NULL,  -- Tamaño máximo recomendado por RFC
    contrasena VARCHAR(255) NOT NULL,     -- Hash de contraseñas
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    telefono CHAR(10)	               -- Exactamente 10 caracteres
);

-- Tabla pagos
CREATE TABLE pagos (
    cedula_administrador CHAR(10),  -- Clave foránea a la tabla administrador
    cedula_propietario CHAR(10),   -- Clave foránea a la tabla propietario
    PRIMARY KEY (cedula_administrador, cedula_propietario),  -- Combinación única de ambas claves
    FOREIGN KEY (cedula_administrador) REFERENCES administrador(numero_de_cedula),  -- Relación con la tabla administrador
    FOREIGN KEY (cedula_propietario) REFERENCES propietario(numero_de_cedula)  -- Relación con la tabla propietario
);

-- Tabla guardia
CREATE TABLE guardia (
    numero_de_cedula CHAR(10) PRIMARY KEY, -- Exactamente 10 caracteres
    correo VARCHAR(320) UNIQUE NOT NULL,  -- Tamaño máximo recomendado por RFC
    contrasena VARCHAR(255) NOT NULL,     -- Hash de contraseñas
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    telefono CHAR(10)	               -- Exactamente 10 caracteres
);

-- Tabla codigoqr
CREATE TABLE codigoqr (
    id INT PRIMARY KEY,  -- Clave primaria 
    cedula_visitante CHAR(10), -- Clave foránea a la tabla visitante
    cedula_propietario CHAR(10),-- Clave foránea a la tabla propietario
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (cedula_visitante) REFERENCES visitante(numero_de_cedula),  -- Relación con la tabla visitante
    FOREIGN KEY (cedula_propietario) REFERENCES propietario(numero_de_cedula)  -- Relación con la tabla propietario
);

-- Tabla preautorizacion
CREATE TABLE preautorizacion (
    id INT PRIMARY KEY,  -- Clave primariapreautorizacion
    cedula_guardia CHAR(10), -- Clave foránea a la tabla guardia
    cedula_visitante CHAR(10), -- Clave foránea a la tabla visitante
    cedula_propietario CHAR(10),-- Clave foránea a la tabla propietario
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (cedula_guardia) REFERENCES guardia(numero_de_cedula),  -- Relación con la tabla guardia
    FOREIGN KEY (cedula_visitante) REFERENCES visitante(numero_de_cedula),  -- Relación con la tabla visitante
    FOREIGN KEY (cedula_propietario) REFERENCES propietario(numero_de_cedula)  -- Relación con la tabla propietario
);

-- Tabla autorizacionguardia
CREATE TABLE autorizacionguardia (
    id INT PRIMARY KEY,  -- Clave primaria
    cedula_guardia CHAR(10), -- Clave foránea a la tabla guardia
    cedula_visitante CHAR(10), -- Clave foránea a la tabla visitante
    codigo_catastral CHAR(25), -- Clave foránea a la tabla casa
    hora TIME,  -- Tipo adecuado para la hora
    fecha DATE, -- Tipo adecuado para la fecha
    FOREIGN KEY (cedula_guardia) REFERENCES guardia(numero_de_cedula),  -- Relación con la tabla guardia
    FOREIGN KEY (cedula_visitante) REFERENCES visitante(numero_de_cedula),  -- Relación con la tabla visitante
    FOREIGN KEY (codigo_catastral) REFERENCES casa(codigo_catastral)  -- Relación con la tabla casa
);








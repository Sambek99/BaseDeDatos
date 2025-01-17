use ciudadela;

-- CREACION DE UN PROCEDIMIENTO QUE REALIZA LA CREACION DE UN CODIGO QR PARA UN USUARIO VERIFICANDO SI EXISTE EL VISITANTE

DELIMITER //
CREATE PROCEDURE insertar_y_generar_qr(
    IN cedula_visitante CHAR(10), 
    IN cedula_propietario CHAR(10), 
    IN nombre VARCHAR(50), 
    IN apellido VARCHAR(50), 
    IN fecha_visita DATE
)
BEGIN
    DECLARE fecha_fin DATE;
    SET fecha_fin = DATE_ADD(fecha_visita, INTERVAL 1 DAY);

    -- Verificar si el visitante existe
    IF NOT EXISTS (SELECT 1 FROM visitante WHERE numero_de_cedula = cedula_visitante) THEN
        -- Insertar un nuevo visitante
        INSERT INTO visitante (numero_de_cedula, nombre, apellido) 
        VALUES (cedula_visitante, nombre, apellido);
    END IF;

    -- Insertar el QR generado
    INSERT INTO codigoqr (cedula_visitante, cedula_propietario, fecha_inicio, fecha_fin)
    VALUES (cedula_visitante, cedula_propietario, fecha_visita, fecha_fin);
END; //
DELIMITER ;

-- SP PARA CREAR AUTORIZACIONES DE LOS PROPIETARIOS
DELIMITER //

CREATE PROCEDURE insertar_y_generar_autorizacion(
    IN cedula_guardia CHAR(10), 
    IN cedula_visitante CHAR(10), 
    IN cedula_propietario CHAR(10),
    IN nombre VARCHAR(50), 
    IN apellido VARCHAR(50),
    IN fecha_visita DATE,
    IN fecha_fin DATE
)
BEGIN
    -- Verificar si el visitante existe
    IF NOT EXISTS (SELECT 1 FROM visitante WHERE numero_de_cedula = cedula_visitante) THEN
        -- Insertar un nuevo visitante
        INSERT INTO visitante (numero_de_cedula, nombre, apellido) 
        VALUES (cedula_visitante, nombre, apellido);
    END IF;

    -- Insertar la autorización en la tabla preautorizacion
    INSERT INTO preautorizacion (cedula_guardia, cedula_visitante, cedula_propietario, fecha_inicio, fecha_fin)
    VALUES (cedula_guardia, cedula_visitante, cedula_propietario, fecha_visita, fecha_fin);
END //

DELIMITER ;


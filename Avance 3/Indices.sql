-- Indices basados en los Querys
use ciudadela;

-- 1. 
-- Optimiza el JOIN entre las tablas propietario y casa mediante numero_de_cedula.
-- indice para busquedas de propietarios en mora

CREATE INDEX idx_propietario_mora_casa ON casa(numero_de_cedula, codigo_catastral, villa, manzana);
CREATE INDEX idx_mora ON propietario(en_mora, numero_de_cedula);

-- 2.
-- Se optimiza la búsqueda por fecha y facilita el JOIN con cedula_visitante.

CREATE INDEX idx_autorizacionguardia_fecha ON autorizacionguardia(fecha, cedula_guardia, cedula_visitante);

-- 3.
-- Optimiza la búsqueda por cedula_propietario y filtra pagos del año 2024.
-- Facilita el LEFT JOIN con la tabla propietario.

CREATE INDEX idx_pagos_fecha_propietario ON pagos(cedula_propietario, fecha_pago, cedula_administrador);
CREATE INDEX idx_propietario_cedula ON propietario(numero_de_cedula, nombre, apellido);

-- 4. 
-- Mejora el JOIN entre vehiculo y casa por codigo_catastral.
-- Optimiza el acceso a información de casa y su propietario.
-- Facilita el acceso a residentes relacionados con una casa específica.

CREATE INDEX idx_vehiculo_codigo_casa ON vehiculo(codigo_catastral, placa, modelo, color);
CREATE INDEX idx_casa_propietario ON casa(codigo_catastral, numero_de_cedula, villa, manzana);
CREATE INDEX idx_residente_codigo_casa ON residente(codigo_catastral, nombre);

-- 5. 
-- Optimiza el filtro por mes (MONTH(pa.fecha_pago) = 3) y el LEFT JOIN.
-- Mejora la recuperación de propietarios que no tienen pagos asociados.

CREATE INDEX idx_pagos_mes ON pagos(cedula_propietario, fecha_pago, cedula_administrador);
CREATE INDEX idx_propietario_sin_pagos ON propietario(numero_de_cedula, nombre, apellido);

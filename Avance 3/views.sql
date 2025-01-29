use ciudadela;
CREATE VIEW HistorialPreAutorizados AS
Select ag.hora hora , ag.fecha fecha, v.nombre "Nombre visita", v.apellido "Apellido visita", ag.codigo_catastral "Codigo Catastral"
FROM visitante v inner join autorizacionguardia ag on v.numero_de_cedula = ag.cedula_visitante 
inner join casa c on c.codigo_catastral = ag.codigo_catastral
ORDER BY ag.fecha DESC;

CREATE VIEW HistorialDePagos as 
Select concat(a.nombre," ",a.apellido) "Nombre Administrador", concat(pr.nombre," ",pr.apellido) "Nombre Propietario", pa.fecha_pago Fecha, pa.monto Monto
FROM pagos pa join administrador a on pa.cedula_administrador = a.numero_de_cedula join propietario pr on pr.numero_de_cedula = pa.cedula_propietario
ORDER BY pa.fecha_pago DESC;

CREATE VIEW HistorialCodigoQR as
SELECT  v.nombre "Nombre visitante" , v.apellido "Apellido visitante", qr.fecha_inicio, qr.fecha_fin, c.codigo_catastral
from codigoqr qr inner join visitante v on v.numero_de_cedula = qr.cedula_visitante 
inner join casa c on c.numero_de_cedula = qr.cedula_propietario
ORDER BY qr.fecha_inicio DESC;

CREATE VIEW ListaNegra as
Select v.numero_de_cedula"Numero de cedula", v.nombre "Nombre", v.apellido "Apellido", c.codigo_catastral "Codigo catastral"
from lista_negra ln join visitante v using numero_de_cedula join casas c using codigo_catastral

DELIMITER //
CREATE PROCEDURE obtenerHistorialPreautorizados(IN numero_de_cedula char(10))
BEGIN 	
Select ag.hora hora , ag.fecha fecha, v.nombre "Nombre visita", v.apellido "Apellido visita"
FROM visitante v inner join autorizacionguardia ag on v.numero_de_cedula = ag.cedula_visitante 
inner join casa c on c.codigo_catastral = ag.codigo_catastral
WHERE c.numero_de_cedula = numero_de_cedula
ORDER BY ag.fecha DESC;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerHistorialCodigoQR(IN cedula_propietario char(10))
BEGIN
SELECT  v.nombre "Nombre visitante" , v.apellido "Apellido visitante", qr.fecha_inicio, qr.fecha_fin, c.codigo_catastral
from codigoqr qr inner join visitante v on v.numero_de_cedula = qr.cedula_visitante 
inner join casa c on c.numero_de_cedula = qr.cedula_propietario
WHERE c.numero_de_cedula = cedula_propietario
ORDER BY qr.fecha_inicio DESC;
END
//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE obtenerHistorialDePagos(IN cedula_propietario char(10))
BEGIN 
Select concat(a.nombre," ",a.apellido) "Nombre Administrador", concat(pr.nombre," ",pr.apellido) "Nombre Propietario", pa.fecha_pago Fecha, pa.monto Monto
FROM pagos pa join administrador a on pa.cedula_administrador = a.numero_de_cedula join propietario pr on pr.numero_de_cedula = pa.cedula_propietario
WHERE pa.cedula_propietario = cedula_propietario
ORDER BY pa.fecha_pago DESC;
END// 
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerListaNegra(IN codigo_catastral char(25))
BEGIN
Select v.numero_de_cedula "Numero de cedula", v.nombre "Nombre", v.apellido "Apellido"
from lista_negra ln join visitante v using (numero_de_cedula) join casas c using (codigo_catastral)
WHERE c.codigo_catastral = codigo_catastral;
END;
//
DELIMITER ;

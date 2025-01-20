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
inner join casa c on c.numero_de_cedula = qr.cedula_propietario;
ORDER BY qr.fecha_inicio DESC;

Delimiter //
CREATE PROCEDURE obtenerHistorialPreautorizados(IN numero_de_cedula char(10))
BEGIN 	
Select ag.hora hora , ag.fecha fecha, v.nombre "Nombre visita", v.apellido "Apellido visita"
FROM visitante v inner join autorizacionguardia ag on v.numero_de_cedula = ag.cedula_visitante 
inner join casa c on c.codigo_catastral = ag.codigo_catastral
WHERE c.numero_de_cedula = numero_de_cedula
ORDER BY ag.fecha DESC;
END//
DELIMITER ;

Delimiter//
CREATE PROCEDURE obtenerHistorialQR(IN cedula_propietario char(10))
BEGIN
SELECT  v.nombre "Nombre visitante" , v.apellido "Apellido visitante", qr.fecha_inicio, qr.fecha_fin, c.codigo_catastral
from codigoqr qr inner join visitante v on v.numero_de_cedula = qr.cedula_visitante 
inner join casa c on c.numero_de_cedula = qr.cedula_propietario;
WHERE c.numero_de_cedula = cedula_propietario
ORDER BY qr.fecha_inicio DESC;
END//
DELIMITER ;


DELIMITER//
CREATE PROCEDURE obtenerHistorialPagos(IN cedula_propietario char(10))
BEGIN 
Select concat(a.nombre," ",a.apellido) "Nombre Administrador", concat(pr.nombre," ",pr.apellido) "Nombre Propietario", pa.fecha_pago Fecha, pa.monto Monto
FROM pagos pa join administrador a on pa.cedula_administrador = a.numero_de_cedula join propietario pr on pr.numero_de_cedula = pa.cedula_propietario
WHERE pa.cedula_propietario = cedula_propietario
ORDER BY pa.fecha_pago DESC;
END// 
DELIMITER ;

CREATE USER 'propietario' IDENTIFIED BY 'Contrapropietario';
GRANT SELECT, INSERT ON ciudadela.propietario TO 'propietario';
GRANT SELECT, INSERT ON ciudadela.casa TO 'propietario';
GRANT SELECT ON ciudadela.HistorialPreAutorizados TO 'propietario';
GRANT EXECUTE ON PROCEDURE obtenerHistorialPreautorizados to 'propietario';
GRANT EXECUTE ON PROCEDURE obtenerHistorialCodigoQR to 'propietario';
GRANT EXECUTE ON PROCEDURE obtenerListaNegra to 'propietario';
GRANT EXECUTE ON PROCEDURE obtenerHistorialPagos to 'propietario';

CREATE USER 'visitante' IDENTIFIED BY 'ContrasenaVisitante';
GRANT SELECT, INSERT ON ciudadela.visitante TO 'visitante';
GRANT SELECT ON ciudadela.lista_negra TO 'visitante';

CREATE USER 'residente' IDENTIFIED BY 'ContraResidente';
GRANT EXECUTE ON ciudadela.insertar_y_generar_qr TO 'residente';
GRANT EXECUTE ON ciudadela.insertar_y_generar_autorizacion TO 'residente';

CREATE USER 'guardia' IDENTIFIED BY 'ContraGuardia';
GRANT SELECT, UPDATE ON ciudadela.autorizacionguardia TO 'guardia';
GRANT SELECT, INSERT ON ciudadela.codigoqr TO 'guardia';
GRANT SELECT ON ciudadela.HistorialDePagos TO 'guardia';

CREATE USER 'administrador' IDENTIFIED BY 'Contramaster';
GRANT ALL PRIVILEGES ON ciudadela.* TO 'administrador';

FLUSH PRIVILEGES;

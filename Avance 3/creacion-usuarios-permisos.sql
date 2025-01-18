CREATE USER 'propietario' IDENTIFIED BY 'Contrapropietario';

CREATE USER 'visitante' IDENTIFIED BY 'ContrasenaVisitante';

CREATE USER 'residente' IDENTIFIED BY 'ContraResidente';
GRANT EXECUTE ON ciudadela.insertar_y_generar_qr TO 'residente';
GRANT EXECUTE ON ciudadela.insertar_y_generar_autorizacion TO 'residente';

CREATE USER 'guardia' IDENTIFIED BY 'ContraGuardia';
GRANT SELECT, UPDATE ON ciudadela.autorizacionguardia TO 'guardia';

CREATE USER 'administrador' IDENTIFIED BY 'Contramaster';
GRANT ALL PRIVILEGES ON ciudadela.* TO 'administrador';

FLUSH PRIVILEGES;
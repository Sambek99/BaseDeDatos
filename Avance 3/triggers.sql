DELIMITER //
CREATE TRIGGER update_en_mora_on_payment
AFTER INSERT ON pagos
FOR EACH ROW
BEGIN
    UPDATE propietario
    SET en_mora = FALSE
    WHERE numero_de_cedula = NEW.cedula_propietario;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER validate_guardia_authorization
BEFORE INSERT ON autorizacionguardia
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1 FROM lista_negra 
        WHERE numero_de_cedula = NEW.cedula_visitante 
        AND codigo_catastral = NEW.codigo_catastral
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Visitor is blacklisted for this house';
    END IF;
END//
DELIMITER ;
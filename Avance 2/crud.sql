use ciudadela;


-- Añadir: se agregaran nuevos inserts

INSERT INTO propietario (numero_de_cedula, correo, contrasena, nombre, apellido, huella_dactilar, telefono, en_mora) VALUES
('0958466578', 'juan_basurita@gmail.com', 'Contra1', 'Juan', 'Basurita', 'huella1', '0911478856', FALSE),
('0996547741', 'marisol_escobar@gmail.com', 'Contra2', 'Marisol', 'Escobar', 'huella2', '0998995621', TRUE),
('0999562114', 'beker_zambrano@gmail.com', 'Contra3', 'Beker', 'Zambrano', 'huella3', '0955124479', FALSE);
('0900000001', 'admin@gmail.com', 'Contramaster', 'Admin', 'Master', 'huella4', '0999999999', FALSE);

INSERT INTO casa (codigo_catastral, numero_de_cedula, villa, manzana, telefono1, telefono2, telefono3) VALUES
('GYE00216', '0958466578', 20, 20, '0911478856', NULL, NULL),
('GYE00217', '0996547741', 21, 22, '0998995621', NULL, NULL),
('GYE00218', '0999562114', 22, 23, '0955124479', NULL, NULL);

INSERT INTO residente (numero_de_cedula, codigo_catastral, nombre, apellido, telefono) VALUES
('0945774682', 'GYE00216', 'Pedro', 'Pascal', '0974584412'),
('0991156062', 'GYE00216', 'Luis', 'Alberto', '0962145987'),
('0969665412', 'GYE00217', 'Luisa', 'Chirivoga', '0932665894'),
('0933248975', 'GYE00218', 'Felipe', 'Crespo', '0921232245');

INSERT INTO visitante (numero_de_cedula, nombre, apellido) VALUES
('0995864512', 'Jefferson', 'Perez'),
('0985696523', 'Victor', 'Manuel'),
('0956892563', 'Loyda', 'Chamba');

INSERT INTO vehiculo (placa, codigo_catastral, modelo, color, matricula) VALUES
('GGE9125', 'GYE00216', 'Toyota Cameron', 'Rosado', '985658'),
('GGE9256', 'GYE00217', 'Nissan Arigato', 'Blanco', '704123'),
('GGE9658', 'GYE00218', 'Chevrolet Sparking', 'Verde', '562356');

INSERT INTO lista_negra (numero_de_cedula, codigo_catastral) VALUES
('0939808859', 'GYE00216'),
('0981125580', 'GYE00217'),
('0973475689', 'GYE00218');

INSERT INTO guardia (numero_de_cedula, correo, contrasena, nombre, apellido, telefono) VALUES
('0901112345', 'first@gmail.com', 'Contra1', 'Juan', 'Perez', '0911478856'),
('0901223456', 'second@gmail.com', 'Contra2', 'Maria', 'Gomez', '0998995621'),
('0901334567', 'three@gmail.com', 'Contra3', 'Pedro', 'Ramirez', '0955124479');

INSERT INTO autorizacionguardia (id, cedula_guardia, cedula_visitante, codigo_catastral, hora, fecha) VALUES
(1, '0901112345', '0995864512', 'GYE00216', '12:00:00', '2024-03-03'),
(2, '0901223456', '0985696523', 'GYE00217', '15:00:00', '2024-04-01'),
(3, '0901334567', '0956892563', 'GYE00218', '09:00:00', '2024-09-12');

-- Juan Basurita: solo pago enero y febrero
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0958466578', '2024-01-05', 55.00), 
       ('0900000001', '0958466578', '2024-02-05', 55.00);

-- Marisol Escobar: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0996547741', '2024-01-05', 55.00), 
       ('0900000001', '0996547741', '2024-02-05', 55.00),
       ('0900000001', '0996547741', '2024-03-05', 55.00),
       ('0900000001', '0996547741', '2024-04-05', 55.00),
       ('0900000001', '0996547741', '2024-05-05', 55.00),
       ('0900000001', '0996547741', '2024-06-05', 55.00),
       ('0900000001', '0996547741', '2024-07-05', 55.00),
       ('0900000001', '0996547741', '2024-08-05', 55.00),
       ('0900000001', '0996547741', '2024-09-05', 55.00),
       ('0900000001', '0996547741', '2024-10-05', 55.00),
       ('0900000001', '0996547741', '2024-11-05', 55.00),
       ('0900000001', '0996547741', '2024-12-05', 55.00);
       
-- Beker Zambrano: Pago octubre y noviembre
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0999562114', '2024-10-05', 55.00),
       ('0900000001', '0999562114', '2024-11-05', 55.00);
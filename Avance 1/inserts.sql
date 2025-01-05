INSERT INTO propietario (numero_de_cedula, correo, contrasena, nombre, apellido, huella_dactilar, telefono, en_mora) VALUES
('0900012345', 'juan.perez@gmail.com', 'hash1', 'Juan', 'Pérez', 'huella1', '0987654321', FALSE),
('0900023456', 'maria.gonzalez@gmail.com', 'hash2', 'María', 'González', 'huella2', '0998765432', TRUE),
('0900034567', 'pedro.rodriguez@gmail.com', 'hash3', 'Pedro', 'Rodríguez', 'huella3', '0982345678', FALSE),
('0900045678', 'ana.lopez@gmail.com', 'hash4', 'Ana', 'López', 'huella4', '0991234567', TRUE),
('0900056789', 'luis.martinez@gmail.com', 'hash5', 'Luis', 'Martínez', 'huella5', '0983123456', FALSE),
('0900067890', 'carmen.sanchez@gmail.com', 'hash6', 'Carmen', 'Sánchez', 'huella6', '0991345678', TRUE),
('0900078901', 'raul.garcia@gmail.com', 'hash7', 'Raul', 'García', 'huella7', '0984567890', FALSE),
('0900089012', 'elena.morales@gmail.com', 'hash8', 'Elena', 'Morales', 'huella8', '0995123456', TRUE),
('0900090123', 'jose.flores@gmail.com', 'hash9', 'José', 'Flores', 'huella9', '0986543210', FALSE),
('0900101234', 'luisa.palacios@gmail.com', 'hash10', 'Luisa', 'Palacios', 'huella10', '0997654321', TRUE);


INSERT INTO casa (codigo_catastral, numero_de_cedula, villa, manzana, telefono1, telefono2, telefono3) VALUES
('GYE00123', '0900012345', 1, 1, '0987654321', NULL, NULL),
('GYE00124', '0900023456', 2, 2, '0998765432', '0982345678', NULL),
('GYE00125', '0900034567', 3, 3, '0983123456', NULL, '0991234567'),
('GYE00126', '0900045678', 4, 4, '0991345678', '0984567890', NULL),
('GYE00127', '0900056789', 5, 5, '0987654321', '0995123456', NULL),
('GYE00128', '0900067890', 6, 6, '0986543210', NULL, NULL),
('GYE00129', '0900078901', 7, 7, '0997654321', '0987654321', '0981234567'),
('GYE00130', '0900089012', 8, 8, '0998765432', NULL, NULL),
('GYE00131', '0900090123', 9, 9, '0982345678', '0992345678', NULL),
('GYE00132', '0900101234', 10, 10, '0986543210', '0993456789', NULL);


INSERT INTO residente (numero_de_cedula, codigo_catastral, nombre, apellido, telefono) VALUES
('0901112345', 'GYE00123', 'Carlos', 'Vega', '0981122334'),
('0901223456', 'GYE00124', 'Laura', 'Rodríguez', '0982233445'),
('0901334567', 'GYE00125', 'Felipe', 'Méndez', '0983344556'),
('0901445678', 'GYE00126', 'Diana', 'Mora', '0984455667'),
('0901556789', 'GYE00127', 'Mario', 'Jiménez', '0985566778'),
('0901667890', 'GYE00128', 'Sandra', 'Figueroa', '0986677889'),
('0901778901', 'GYE00129', 'Roberto', 'Castillo', '0987788990'),
('0901889012', 'GYE00130', 'Rosa', 'Gómez', '0988899001'),
('0901990123', 'GYE00131', 'Juan', 'Serrano', '0989900112'),
('0902001234', 'GYE00132', 'José', 'Ramírez', '0990011223');


INSERT INTO visitante (numero_de_cedula, nombre, apellido) VALUES
('0902112345', 'Pedro', 'Alvarado'),
('0902223456', 'Lucía', 'Martínez'),
('0902334567', 'Eduardo', 'Castro'),
('0902445678', 'Marina', 'Paredes'),
('0902556789', 'Ricardo', 'López'),
('0902667890', 'Andrea', 'Ramón'),
('0902778901', 'Esteban', 'González'),
('0902889012', 'Celia', 'Serrano'),
('0902990123', 'Fernando', 'Ruíz'),
('0903001234', 'Marta', 'Rodríguez');


INSERT INTO vehiculo (placa, codigo_catastral, modelo, color, matricula) VALUES
('GGE1234', 'GYE00123', 'Toyota Corolla', 'Blanco', '123456'),
('GGE2345', 'GYE00124', 'Nissan X-Trail', 'Negro', '234567'),
('GGE3456', 'GYE00125', 'Chevrolet Aveo', 'Rojo', '345678'),
('GGE4567', 'GYE00126', 'Hyundai Tucson', 'Azul', '456789'),
('GGE5678', 'GYE00127', 'Mazda CX-5', 'Gris', '567890'),
('GGE6789', 'GYE00128', 'Kia Sportage', 'Plata', '678901'),
('GGE7890', 'GYE00129', 'Honda CR-V', 'Verde', '789012'),
('GGE8901', 'GYE00130', 'Ford Escape', 'Amarillo', '890123'),
('GGE9012', 'GYE00131', 'Mitsubishi Outlander', 'Rojo', '901234'),
('GGE0123', 'GYE00132', 'Subaru Forester', 'Blanco', '012345');


INSERT INTO lista_negra (numero_de_cedula, codigo_catastral) VALUES
('0902112345', 'GYE00123'),
('0902223456', 'GYE00124'),
('0902334567', 'GYE00125'),
('0902445678', 'GYE00126'),
('0902556789', 'GYE00127'),
('0902667890', 'GYE00128'),
('0902778901', 'GYE00129'),
('0902889012', 'GYE00130'),
('0902990123', 'GYE00131'),
('0903001234', 'GYE00132');


INSERT INTO codigoqr (id, cedula_visitante, cedula_propietario, fecha_inicio, fecha_fin) VALUES
(1, '0902112345', '0900012345', '2024-01-01', '2024-01-15'),
(2, '0902223456', '0900023456', '2024-01-10', '2024-01-20'),
(3, '0902334567', '0900034567', '2024-01-15', '2024-01-25'),
(4, '0902445678', '0900045678', '2024-02-01', '2024-02-10'),
(5, '0902556789', '0900056789', '2024-02-15', '2024-02-28'),
(6, '0902667890', '0900067890', '2024-03-01', '2024-03-15'),
(7, '0902778901', '0900078901', '2024-03-10', '2024-03-20'),
(8, '0902889012', '0900089012', '2024-03-15', '2024-03-30'),
(9, '0902990123', '0900090123', '2024-04-01', '2024-04-10'),
(10, '0903001234', '0900101234', '2024-04-05', '2024-04-15');


INSERT INTO preautorizacion (id, cedula_guardia, cedula_visitante, cedula_propietario, fecha_inicio, fecha_fin) VALUES
(1, '0901112345', '0902112345', '0900012345', '2024-01-01', '2024-01-15'),
(2, '0901223456', '0902223456', '0900023456', '2024-01-10', '2024-01-20'),
(3, '0901334567', '0902334567', '0900034567', '2024-01-15', '2024-01-25'),
(4, '0901445678', '0902445678', '0900045678', '2024-02-01', '2024-02-10'),
(5, '0901556789', '0902556789', '0900056789', '2024-02-15', '2024-02-28'),
(6, '0901667890', '0902667890', '0900067890', '2024-03-01', '2024-03-15'),
(7, '0901778901', '0902778901', '0900078901', '2024-03-10', '2024-03-20'),
(8, '0901889012', '0902889012', '0900089012', '2024-03-15', '2024-03-30'),
(9, '0901990123', '0902990123', '0900090123', '2024-04-01', '2024-04-10'),
(10, '0902001234', '0903001234', '0900101234', '2024-04-05', '2024-04-15');


INSERT INTO autorizacionguardia (id, cedula_guardia, cedula_visitante, codigo_catastral, hora, fecha) VALUES
(1, '0901112345', '0902112345', 'GYE00123', '08:00:00', '2024-01-01'),
(2, '0901223456', '0902223456', 'GYE00124', '09:00:00', '2024-01-10'),
(3, '0901334567', '0902334567', 'GYE00125', '10:00:00', '2024-01-15'),
(4, '0901445678', '0902445678', 'GYE00126', '11:00:00', '2024-02-01'),
(5, '0901556789', '0902556789', 'GYE00127', '12:00:00', '2024-02-15'),
(6, '0901667890', '0902667890', 'GYE00128', '13:00:00', '2024-03-01'),
(7, '0901778901', '0902778901', 'GYE00129', '14:00:00', '2024-03-10'),
(8, '0901889012', '0902889012', 'GYE00130', '15:00:00', '2024-03-15'),
(9, '0901990123', '0902990123', 'GYE00131', '16:00:00', '2024-04-01'),
(10, '0902001234', '0903001234', 'GYE00132', '17:00:00', '2024-04-05');


-- Pagos para propietarios con en_mora = TRUE (12 pagos por año)
-- Propietarios en mora: '0900023456', '0900045678', '0900067890', '0900089012', '0900101234'

-- Juan Pérez: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900012345', '2024-01-05', 55.00), 
       ('0900000001', '0900012345', '2024-02-05', 55.00),
       ('0900000001', '0900012345', '2024-03-05', 55.00),
       ('0900000001', '0900012345', '2024-04-05', 55.00),
       ('0900000001', '0900012345', '2024-05-05', 55.00),
       ('0900000001', '0900012345', '2024-06-05', 55.00),
       ('0900000001', '0900012345', '2024-07-05', 55.00),
       ('0900000001', '0900012345', '2024-08-05', 55.00),
       ('0900000001', '0900012345', '2024-09-05', 55.00),
       ('0900000001', '0900012345', '2024-10-05', 55.00),
       ('0900000001', '0900012345', '2024-11-05', 55.00),
       ('0900000001', '0900012345', '2024-12-05', 55.00);

-- María González: Faltan los meses de Junio y Julio
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900023456', '2024-01-05', 55.00), 
       ('0900000001', '0900023456', '2024-02-05', 55.00),
       ('0900000001', '0900023456', '2024-03-05', 55.00),
       ('0900000001', '0900023456', '2024-04-05', 55.00),
       ('0900000001', '0900023456', '2024-05-05', 55.00),
       ('0900000001', '0900023456', '2024-08-05', 55.00),
       ('0900000001', '0900023456', '2024-09-05', 55.00),
       ('0900000001', '0900023456', '2024-10-05', 55.00),
       ('0900000001', '0900023456', '2024-11-05', 55.00),
       ('0900000001', '0900023456', '2024-12-05', 55.00);

-- Pedro Rodríguez: Faltan los meses de Marzo, Abril y Mayo
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900034567', '2024-01-05', 55.00), 
       ('0900000001', '0900034567', '2024-02-05', 55.00),
       ('0900000001', '0900034567', '2024-06-05', 55.00),
       ('0900000001', '0900034567', '2024-07-05', 55.00),
       ('0900000001', '0900034567', '2024-08-05', 55.00),
       ('0900000001', '0900034567', '2024-09-05', 55.00),
       ('0900000001', '0900034567', '2024-10-05', 55.00),
       ('0900000001', '0900034567', '2024-11-05', 55.00),
       ('0900000001', '0900034567', '2024-12-05', 55.00);

-- Ana López: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900045678', '2024-01-05', 55.00), 
       ('0900000001', '0900045678', '2024-02-05', 55.00),
       ('0900000001', '0900045678', '2024-03-05', 55.00),
       ('0900000001', '0900045678', '2024-04-05', 55.00),
       ('0900000001', '0900045678', '2024-05-05', 55.00),
       ('0900000001', '0900045678', '2024-06-05', 55.00),
       ('0900000001', '0900045678', '2024-07-05', 55.00),
       ('0900000001', '0900045678', '2024-08-05', 55.00),
       ('0900000001', '0900045678', '2024-09-05', 55.00),
       ('0900000001', '0900045678', '2024-10-05', 55.00),
       ('0900000001', '0900045678', '2024-11-05', 55.00),
       ('0900000001', '0900045678', '2024-12-05', 55.00);

-- Luis Martínez: Faltan los meses de Octubre, Noviembre y Diciembre
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900056789', '2024-01-05', 55.00), 
       ('0900000001', '0900056789', '2024-02-05', 55.00),
       ('0900000001', '0900056789', '2024-03-05', 55.00),
       ('0900000001', '0900056789', '2024-04-05', 55.00),
       ('0900000001', '0900056789', '2024-05-05', 55.00),
       ('0900000001', '0900056789', '2024-06-05', 55.00),
       ('0900000001', '0900056789', '2024-07-05', 55.00),
       ('0900000001', '0900056789', '2024-08-05', 55.00),
       ('0900000001', '0900056789', '2024-09-05', 55.00);

-- Carmen Sánchez: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900067890', '2024-01-05', 55.00), 
       ('0900000001', '0900067890', '2024-02-05', 55.00),
       ('0900000001', '0900067890', '2024-03-05', 55.00),
       ('0900000001', '0900067890', '2024-04-05', 55.00),
       ('0900000001', '0900067890', '2024-05-05', 55.00),
       ('0900000001', '0900067890', '2024-06-05', 55.00),
       ('0900000001', '0900067890', '2024-07-05', 55.00),
       ('0900000001', '0900067890', '2024-08-05', 55.00),
       ('0900000001', '0900067890', '2024-09-05', 55.00),
       ('0900000001', '0900067890', '2024-10-05', 55.00),
       ('0900000001', '0900067890', '2024-11-05', 55.00),
       ('0900000001', '0900067890', '2024-12-05', 55.00);

-- Raúl García: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900078901', '2024-01-05', 55.00), 
       ('0900000001', '0900078901', '2024-02-05', 55.00),
       ('0900000001', '0900078901', '2024-03-05', 55.00),
       ('0900000001', '0900078901', '2024-04-05', 55.00),
       ('0900000001', '0900078901', '2024-05-05', 55.00),
       ('0900000001', '0900078901', '2024-06-05', 55.00),
       ('0900000001', '0900078901', '2024-07-05', 55.00),
       ('0900000001', '0900078901', '2024-08-05', 55.00),
       ('0900000001', '0900078901', '2024-09-05', 55.00),
       ('0900000001', '0900078901', '2024-10-05', 55.00),
       ('0900000001', '0900078901', '2024-11-05', 55.00),
       ('0900000001', '0900078901', '2024-12-05', 55.00);

-- Elena Morales: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900089012', '2024-01-05', 55.00), 
       ('0900000001', '0900089012', '2024-02-05', 55.00),
       ('0900000001', '0900089012', '2024-03-05', 55.00),
       ('0900000001', '0900089012', '2024-04-05', 55.00),
       ('0900000001', '0900089012', '2024-05-05', 55.00),
       ('0900000001', '0900089012', '2024-06-05', 55.00),
       ('0900000001', '0900089012', '2024-07-05', 55.00),
       ('0900000001', '0900089012', '2024-08-05', 55.00),
       ('0900000001', '0900089012', '2024-09-05', 55.00),
       ('0900000001', '0900089012', '2024-10-05', 55.00),
       ('0900000001', '0900089012', '2024-11-05', 55.00),
       ('0900000001', '0900089012', '2024-12-05', 55.00);

-- José Flores: Completo los 12 meses
INSERT INTO pagos (cedula_administrador, cedula_propietario, fecha_pago, monto)
VALUES ('0900000001', '0900090123', '2024-01-05', 55.00), 
       ('0900000001', '0900090123', '2024-02-05', 55.00),
       ('0900000001', '0900090123', '2024-03-05', 55.00),
       ('0900000001', '0900090123', '2024-04-05', 55.00),
       ('0900000001', '0900090123', '2024-05-05', 55.00),
       ('0900000001', '0900090123', '2024-06-05', 55.00),
       ('0900000001', '0900090123', '2024-07-05', 55.00),
       ('0900000001', '0900090123', '2024-08-05', 55.00),
       ('0900000001', '0900090123', '2024-09-05', 55.00),
       ('0900000001', '0900090123', '2024-10-05', 55.00),
       ('0900000001', '0900090123', '2024-11-05', 55.00),
       ('0900000001', '0900090123', '2024-12-05', 55.00);



INSERT INTO administrador (numero_de_cedula, correo, contrasena, nombre, apellido, telefono) VALUES
('0900000001', 'admin@gmail.com', 'admin1234', 'Juan', 'Perez', '0987654321');


INSERT INTO guardia (numero_de_cedula, correo, contrasena, nombre, apellido, telefono) VALUES
('0901112345', 'guardia1@gmail.com', 'guardia123', 'Carlos', 'Sánchez', '0981234567'),
('0901223456', 'guardia2@gmail.com', 'guardia124', 'Ana', 'González', '0982345678'),
('0901334567', 'guardia3@gmail.com', 'guardia125', 'Pedro', 'Martínez', '0983456789'),
('0901445678', 'guardia4@gmail.com', 'guardia126', 'Luisa', 'Ramírez', '0984567890'),
('0901556789', 'guardia5@gmail.com', 'guardia127', 'Javier', 'López', '0985678901'),
('0901667890', 'guardia6@gmail.com', 'guardia128', 'Marta', 'Hernández', '0986789012'),
('0901778901', 'guardia7@gmail.com', 'guardia129', 'José', 'Pérez', '0987890123'),
('0901889012', 'guardia8@gmail.com', 'guardia130', 'Laura', 'Díaz', '0988901234'),
('0901990123', 'guardia9@gmail.com', 'guardia131', 'Raúl', 'Gómez', '0989012345'),
('0902001234', 'guardia10@gmail.com', 'guardia132', 'Isabel', 'Vargas', '0980123456');


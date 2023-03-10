

CREATE TABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    server_id INTEGER NOT NULL,
    server_name VARCHAR(255) NOT NULL,
    owner_id INTEGER NOT NULL,
    main_channel_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS nitrado_servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    server_id INTEGER NOT NULL,
    nitrado_server_id INTEGER NOT NULL UNIQUE,
    nitrado_server_name VARCHAR(255) NOT NULL,
    encrypted_key BLOB NOT NULL,
    ciphertext BLOB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tp_coord (
	realm TEXT NOT NULL,
	direction TEXT NOT NULL,
	lat	REAL NOT NULL,
	long REAL NOT NULL
)

INSERT INTO tp_coord VALUES
('Jotunheim ','Jotunheim ','North ','56.5','38.9'),
('Jotunheim ','Jotunheim ','North-East ','61.2','54.4'),
('Jotunheim ','Jotunheim ','East ','84.8','57.2'),
('Jotunheim ','Jotunheim ','South-East ','84.1','55.8'),
('Jotunheim ','Jotunheim ','South ','92.2','43.1'),
('Jotunheim ','Jotunheim ','South-West ','89.8','26.8'),
('Jotunheim ','Jotunheim ','West ','68.6','24.1'),
('Jotunheim ','Jotunheim ','North-West ','67.9','25.0'),
('Asgard ','Asgard ','North ','17.9','30.2'),
('Asgard ','Asgard ','North-East ','19.0','42.3'),
('Asgard ','Asgard ','East ','54.4','47.9'),
('Asgard ','Asgard ','South-East ','64.7','39.1'),
('Asgard ','Asgard ','South ','65.5','15.0'),
('Asgard ','Asgard ','South-West ','64.8','10.6'),
('Asgard ','Asgard ','West ','47.1','5.9'),
('Asgard ','Asgard ','North-West ','20.3','12.6'),
('Vanaheim ','Vanaheim ','North ','0.0','98.7'),
('Vanaheim ','Vanaheim ','North-East ','0.0','99.1'),
('Vanaheim ','Vanaheim ','East ','0.9','99.9'),
('Vanaheim ','Vanaheim ','South-East ','20.3','96.3'),
('Vanaheim ','Vanaheim ','South ','32.3','81.8'),
('Vanaheim ','Vanaheim ','South-West ','30.5','67.9'),
('Vanaheim ','Vanaheim ','West ','10.1','65.6'),
('Vanaheim ','Vanaheim ','North-West ','1.6','66.6'),
('Balheimr ','Balheimr ','North ','70.0','89.8'),
('Balheimr ','Balheimr ','North-East ','72.2','96.7'),
('Balheimr ','Balheimr ','East ','72.4','95.9'),
('Balheimr ','Balheimr ','South-East ','96.9','78.5'),
('Balheimr ','Balheimr ','South ','95.9','74.7'),
('Balheimr ','Balheimr ','South-West ','91.7','69.6'),
('Balheimr ','Balheimr ','West ','82.1','70.3'),
('Balheimr ','Balheimr ','North-West ','75.6','77.7'),
('Vannaland ','Vannaland West ','North ','21.1','4.3'),
('Vannaland ','Vannaland West ','North-East ','32.8','32.4'),
('Vannaland ','Vannaland West ','East ','32.8','31.7'),
('Vannaland ','Vannaland West ','South-East ','32.8','32.4'),
('Vannaland ','Vannaland West ','South ','36.3','22.9'),
('Vannaland ','Vannaland West ','South-West ','28.6','7.1'),
('Vannaland ','Vannaland West ','West ','21.1','04.3'),
('Vannaland ','Vannaland West ','North-West ','23.3','4.5'),
('Vannaland ','Vannaland South','North ','28.9','94.9'),
('Vannaland ','Vannaland South','North-East ','29.5','97.8'),
('Vannaland ','Vannaland South','East ','45.9','98.2'),
('Vannaland ','Vannaland South','South-East ','60.0','87.6'),
('Vannaland ','Vannaland South','South ','67.5','72.7'),
('Vannaland ','Vannaland South','South-West ','45.5','49.8'),
('Vannaland ','Vannaland South','West ','45.5','49.8'),
('Vannaland ','Vannaland South','North-West ','45.5','49.8'),
('Vannaland ','Vannaland East','North ','5.9','79.4'),
('Vannaland ','Vannaland East','North-East ','9.3','96.7'),
('Vannaland ','Vannaland East','East ','17.2','98.8'),
('Vannaland ','Vannaland East','South-East ','25.4','97.3'),
('Vannaland ','Vannaland East','South ','25.8','95.3'),
('Vannaland ','Vannaland East','South-West ','25.8','95.3'),
('Vannaland ','Vannaland East','West ','5.9','79.4'),
('Vannaland ','Vannaland East','North-West ','05.9','79.4'),
('Vannaland ','Vannaland North','North ','1.4','59.8'),
('Vannaland ','Vannaland North','North-East ','4.5','75.4'),
('Vannaland ','Vannaland North','East ','4.5','75.4'),
('Vannaland ','Vannaland North','South-East ','4.5','75.4'),
('Vannaland ','Vannaland North','South ','7.7','3.8'),
('Vannaland ','Vannaland North','South-West ','07.7','3.8'),
('Vannaland ','Vannaland North','West ','7.7','3.8'),
('Vannaland ','Vannaland North','North-West ','3.8','6.8'),
('Vardiland ','Vardiland South','North ','81.8','45.6'),
('Vardiland ','Vardiland South','North-East ','81.8','45.6'),
('Vardiland ','Vardiland South','East ','81.8','45.6'),
('Vardiland ','Vardiland South','South-East ','94.8','37.6'),
('Vardiland ','Vardiland South','South ','99.1','8.6'),
('Vardiland ','Vardiland South','South-West ','97.3','6.2'),
('Vardiland ','Vardiland South','West ','85.5','2.7'),
('Vardiland ','Vardiland South','North-West ','85.5','2.7'),
('Vardiland ','Vardiland North','North ','53.0','29.9'),
('Vardiland ','Vardiland North','North-East ','53.7','31.8'),
('Vardiland ','Vardiland North','East ','71.4','40.0'),
('Vardiland ','Vardiland North','South-East ','71.4','40.0'),
('Vardiland ','Vardiland North','South ','71.4','40.0'),
('Vardiland ','Vardiland North','South-West ','66.9','2.4'),
('Vardiland ','Vardiland North','West ','65.3','02.4'),
('Vardiland ','Vardiland North','North-West ','62.1','3.5');


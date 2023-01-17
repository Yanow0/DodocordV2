

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

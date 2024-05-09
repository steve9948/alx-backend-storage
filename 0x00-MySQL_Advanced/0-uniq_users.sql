-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255)
)

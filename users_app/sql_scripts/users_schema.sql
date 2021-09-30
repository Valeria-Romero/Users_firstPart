CREATE DATABASE users_schema;

USE users_schema;

CREATE TABLE users(
	id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(45),
    created_at DATETIME,
    updated_at DATETIME
);

INSERT INTO users(id,first_name,last_name,email,created_at,updated_at)
VALUES 	(01,'Max', 'Rodriguez','max.andres_rf@gmail.com',SYSDATE(),SYSDATE()),
		(02,'Javier', 'Baimason','baimason@hotmail.com',SYSDATE(),SYSDATE()),
        (03, 'Sergio', 'Fernandez', 'fernandez.sergio32@gmail.com',SYSDATE(),SYSDATE());



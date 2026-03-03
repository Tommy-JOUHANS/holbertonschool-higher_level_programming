-- Creates the table id_not_null on your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
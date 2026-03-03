-- Creates a MySQL user named user_0d_1 with password user_0d_1_pwd and grants all privileges on the database database_0d_1 to this user.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON `database_0d_1`. * TO 'user_0d_1'@'localhost';

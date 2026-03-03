-- Create the database named hbtn__0d2 and the user user_0d_2 with password user_0d_2_pwd
-- User_0d_2 should have all SELECT privileges on the database hbtn__0d2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn__0d2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn__0d2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn__0d2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

CREATE database karaage;
CREATE USER 'karaage'@'localhost' IDENTIFIED BY '@database_password@';
GRANT ALL PRIVILEGES ON karaage.* TO 'karaage'@'localhost';

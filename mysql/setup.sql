CREATE database karaage;
CREATE USER 'karaage'@'localhost' IDENTIFIED BY 'mysqlsecret';
GRANT ALL PRIVILEGES ON karaage.* TO 'karaage'@'localhost';

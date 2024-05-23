-- Lists all privileges of the MySQL user `user_0d_1` on your server (in localhost).
SHOW GRANTS FOR `user_0d_1`@`localhost`;

-- Lists all privileges of the MySQL user `user_0d_2` on your server (in localhost).
SHOW GRANTS FOR `user_0d_2`@`localhost`;

-- Refresh the privileges to ensure that any changes made manually are applied.
FLUSH PRIVILEGES;

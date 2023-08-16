-- creates the MySQL server user user_0d_1
-- access pass: user_0d_1_pwd
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- gives all privileges to user user_0d_1
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;


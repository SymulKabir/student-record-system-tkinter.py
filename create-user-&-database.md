## Create a New MySQL User
Open your terminal and log into MySQL as root:
```bash
mysql -u root -p
```
Then run these commands:

#### Create the user
Use `%` when you need to connect database remotely
```SQL
CREATE USER 'nextuser'@'%' IDENTIFIED BY 'StrongPassword123!';
```
**OR** 
If you are useing Docker
```SQL
CREATE USER 'nextuser'@'localhost' IDENTIFIED BY 'StrongPassword123!';
```
 
#### Create database & Grant permissions
```SQL
CREATE DATABASE your_database_name;
SHOW DATABASES; 
GRANT ALL PRIVILEGES ON *.* TO 'nextuser'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

#### Test the user
```SQL
mysql -u nextuser -p
```
Then enter your password

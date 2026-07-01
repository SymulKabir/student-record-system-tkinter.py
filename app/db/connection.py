import mysql.connector

import mysql.connector

db_instance = mysql.connector.connect(
  host="127.0.0.1",
  user="nextuser",
  password="StrongPassword123!",
  database="student"
)


db = db_instance.cursor()
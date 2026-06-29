import mysql.connector

import mysql.connector

db_instance = mysql.connector.connect(
  host="localhost",
  user="taskflow_user",
  password="12345",
  database="taskflow"
)


db = db_instance.cursor()
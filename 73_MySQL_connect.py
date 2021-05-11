import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="Mahedi", password="7845", database="cs50")

mycursor = mydb.cursor()

mycursor.execute("select * from student_info")

for i in mycursor:
	print(i)

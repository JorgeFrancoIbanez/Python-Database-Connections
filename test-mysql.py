import mysql.connector

mydb = mysql.connector.connect(
	host='<HOST>',
	user='<USERNAME>',
	password='<PASSWORD>',
	database='<DATABASE_NAME>')
mycursor=mydb.cursor()
print(mycursor.execute("show databases;"))

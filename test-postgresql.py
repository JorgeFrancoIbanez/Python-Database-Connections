import psycopg2 as psy

try: 
	string="host='<HOST>' dbname='<DATABASE_NAME>' user='<USERNAME>' password='<PASSWORD>'"
	print("connecting")
	connection= psy.connect(string)
	print("connected")
	cursor = connection.cursor()

	cursor.execute("select version();")
	record = cursor.fetchone()
	print(record)
	cursor.close()
	connection.close()
except:
	print("error")

import redis

try:
	conn= redis.StrictRedis(
		host='<HOST>',
		port='<PORT>',
		password=None #you can set a password to access the database. If not by default leave None as value
		)
	print conn
	conn.ping()
	print('Connected')
except Exception as ex:
	print('Error', ex)
	exit('Connection Failed.')

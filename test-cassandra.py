from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cluster  = Cluster(['<HOST>'], auth_provider=PlainTextAuthProvider(username='<USERNAME>',password='<PASSWORD>'), protocol_version=2)
session = cluster.connect()
print('ConnectING to a valide keyspace')
row = session.execute('use <KEYSPACE>')
print(row)
print('Available keyspace')
row = session.execute('select * from system.schema_keyspaces')
for i in row:
	print(i)

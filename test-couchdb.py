import couchdb
couch = couchdb.Server('http://<USERNAME>:<PASSWORD>@<HOST>:<PORT>')
db = couch['<DATABASE_NAME>']
print db
for i in db:
	print i

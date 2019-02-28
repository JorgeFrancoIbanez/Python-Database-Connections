from pymongo import MongoClient

#CONNECT AS USER WITH ADMIN PRIVILEGES 
client = MongoClient('mongodb://<USERNAME>:<PASSWORD>@<HOST>/<DABTASE_NAME>?authSource=admin')
db = client.get_database()  
print(db.collection)

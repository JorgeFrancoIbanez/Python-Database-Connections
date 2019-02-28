import sys
from couchbase.cluster import Cluster, PasswordAuthenticator

cluster = Cluster('couchbase://<HOST>:<PORT>')
print("connecting")
cluster.authenticate(PasswordAuthenticator('<USERNAME>','<PASSWORD>'))
cb = cluster.open_bucket('<BUCKET>')

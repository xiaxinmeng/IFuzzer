import bsddb
d = bsddb.hashopen('a.db', 'c')
d.close()
while True:
    d = bsddb.hashopen('a.db')
    d.close()
db = dumb.open('test_db', 'c')
print(db['a'])
db.close()
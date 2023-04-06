import dbm.dumb as dumb

db = dumb.open('test_db', 'c')
db.clear()
db['a'] = 'a'
db.sync()
db['a'] = 'aa'
abort()
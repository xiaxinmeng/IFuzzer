import sqlite3
db = sqlite3.connect(':memory:')
cur = db.cursor()
cur.execute("create table foo (x)")
# this works fine
cur.execute(u"insert into foo values ('café')".encode('latin1'))
# this fails
cur.execute(u"insert into foo values (?)", (u'café'.encode('latin1'),))
# this fails too
cur.execute("insert into foo values (?)", (u'café'.encode('latin1'),))
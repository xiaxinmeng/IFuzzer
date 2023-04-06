import sqlite3, datetime
c = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = c.cursor()
cur.execute('create table test(t timestamp)')
t = datetime.datetime.now(tz=datetime.timezone.utc)
cur.execute("insert into test(t) values (?)", (t,))
cur.execute('select t from test')
l = cur.fetchone()[0]
t == l   # the result not equal to the original one
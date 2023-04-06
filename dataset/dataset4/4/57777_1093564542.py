import sqlite3
d = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
c = d.cursor()
c.execute("create table testdate (t1 date)")
c.execute("insert into testdate values ('now')")
c.execute("select * from testdate")
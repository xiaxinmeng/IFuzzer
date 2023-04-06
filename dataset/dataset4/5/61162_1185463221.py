db = sqlite3.connect("x.db")
db.execute("create table foo(x);") # this auto-commits, as expected. `$ sqlite3 x.db .dump` shows the table as expected.
db.execute("insert into foo values (1);") # this implicitly creates a cursor and a transaction but doesn't commit it!!
db.close()
# $ sqlite3 x.db .dump # the table is empty! why?
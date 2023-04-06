c1 = conn1.cursor()
c1.execute("select * from foo where id=1")
row1 = c1.fetchone()
c1.close()

conn2 = sqlite3.connect("file.db")
c2 = conn2.cursor()

c2.execute("PRAGMA read_uncommitted=SERIALIZABLE")

# sqlite3 should be doing this automatically.
# when called, conn1's commit blocks
#c2.execute("BEGIN")
c2.execute("select * from foo where id=1")
row2 = c2.fetchone()
c2.close()

c1 = conn1.cursor()
c1.execute("update foo set data='data2'")
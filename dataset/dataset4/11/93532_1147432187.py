import sqlite3
cursor = sqlite3.connect(":memory:", isolation_level=None).cursor()

cursor.execute("""CREATE TABLE foo (id INTEGER)""")

values = ((1,), (2,), (3,))
cursor.executemany("""INSERT INTO foo (id) VALUES (?)""", values)

cursor.execute("vacuum")
print(cursor.rowcount)
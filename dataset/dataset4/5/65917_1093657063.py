import sqlite3
conn = sqlite3.connect(":memory:")

cursor = conn.cursor()
cursor.execute("""
    create table foo (id integer primary key, data varchar(20))
""")
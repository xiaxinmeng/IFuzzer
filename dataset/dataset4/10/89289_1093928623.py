import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.execute('CREATE TABLE foo (bar)')

try:
    conn.__init__('/bad-file/')
except sqlite3.OperationalError:
    pass

cursor.execute('INSERT INTO foo (bar) VALUES (1), (2), (3), (4)')
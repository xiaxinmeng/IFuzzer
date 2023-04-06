import sqlite3
conn = sqlite3.connect(':memory:')
conn.execute('/* comment */ vacuum')
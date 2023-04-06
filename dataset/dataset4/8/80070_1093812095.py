import sqlite3
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
print(conn.execute("SELECT 'John' AS name, 42 AS salary").fetchone())
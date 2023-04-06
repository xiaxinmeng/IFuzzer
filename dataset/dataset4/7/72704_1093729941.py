conn = sqlite3.connect(':memory:', isolation_level='IMMEDIATE')
conn.execute('begin immediate')
cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
row = cur.fetchone()
print(row.keys())

cur.execute('select current_date as "nit [date]", current_timestamp as "nit [timestamp]"')
row = cur.fetchone()
print(row.keys())

cur.execute('select current_date as " [date]", current_timestamp as " [timestamp]"')
row = cur.fetchone()
print(row.keys())
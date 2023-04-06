data = bytes(range(256))
cursor.execute(u"INSERT INTO t (blob_col) values (%(data)s)", {"data": data})
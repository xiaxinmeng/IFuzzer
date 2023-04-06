db = sqlite3.connect(..., isolation_level=None, factory=ConnectionFixedCtxManager)

with db.transaction() as cursor:
    cursor.execute("insert into foo values (1);")

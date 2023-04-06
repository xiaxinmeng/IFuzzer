connection = sqlite3.connect(":memory:")
cursor = sqlite3.Cursor(connection)
ref = weakref.ref(cursor, callback)
cursor.__init__(connection)
del cursor
del ref
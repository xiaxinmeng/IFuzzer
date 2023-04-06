import sqlite3
cx = sqlite3.connect(":memory:")
lim = cx.SQLITE_LIMIT_LENGTH
cx.SQLITE_LIMIT_LENGTH = 100

# instead of
lim = cx.getlimit(sqlite3.SQLITE_LIMIT_LENGTH)
cx.setlimit(sqlite3.SQLITE_LIMIT_LENGTH, 100)
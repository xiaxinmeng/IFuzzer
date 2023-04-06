import sqlite3
cx = sqlite3.connect(":memory:")
cx.set_trace_callback(print)
cx.setlimit(sqlite3.SQLITE_LIMIT_LENGTH, 7)
cx.execute("select ?", ("a"*10,))
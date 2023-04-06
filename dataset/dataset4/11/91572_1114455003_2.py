import sqlite3
cx = sqlite3.connect(":memory:")
val = dict()
cx.execute("select ?", (val,))
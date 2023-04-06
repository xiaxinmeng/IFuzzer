
data = [
    ("row1",),
    ("row2",),
]
cur.executemany("insert into t values(?)", data)

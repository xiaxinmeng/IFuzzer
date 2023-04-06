import sqlite3
import sys
import os

con = sqlite3.connect(":memory:")
con.text_factory = os.fsdecode

con.create_function("py_identity", 1, lambda x: x)

cur = con.cursor()
cur.execute("CREATE TABLE foo(bar TEXT)")
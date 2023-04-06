import sqlite3
import os

if os.path.exists("file.db"):
    os.unlink("file.db")
    
conn1 = sqlite3.connect("file.db")

c1 = conn1.cursor()

c1.execute("PRAGMA read_uncommitted=SERIALIZABLE")
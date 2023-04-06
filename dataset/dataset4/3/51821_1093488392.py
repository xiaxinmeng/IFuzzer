import sqlite3
def loopy():
	return 'OSS'
#get connection object 
conn = sqlite3.connect("/tmp/example")
#get curson obj. and invoke execute
cur = conn.cursor()

conn.create_function("loopy",0,loopy)
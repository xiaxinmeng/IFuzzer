import sqlite3
def loopy():
	return 'GNU'
#get connection object 
conn = sqlite3.connect("/tmp/example2")
#get curson obj. and invoke execute
cur = conn.cursor()
cur.execute('''create table stk (txt text)''')
#insert a single record
conn.create_function("loopy",0,loopy)
t=(loopy(),)
cur.execute("insert into stk values (?)",t)
#I have close it without committing. -So my record length == 0
cur.close()
#But when  i open again new cursor cur1
cur1=conn.cursor()
cur1.execute("select * from stk")
row = cur1.fetchall()
# i expect this assert to pass - since there is no record 
assert len(row) < 1
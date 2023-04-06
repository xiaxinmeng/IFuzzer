import sqlite3
con = sqlite3.connect('/tmp/test.db')
with con:                                                        
    con.execute("insert into person(firstname) values (?)", ("Jan",))
    pass
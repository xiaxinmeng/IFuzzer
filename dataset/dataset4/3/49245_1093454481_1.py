import sqlite3
cn=sqlite3.connect(':memory:')
c=cn.cursor()
c.execute('BEGIN TRANSACTION')
c.execute('create temp table tmp_main (id integer, b text)')
cn.commit() # this was added on your request
c.execute('insert into tmp_main (id) values (10);')
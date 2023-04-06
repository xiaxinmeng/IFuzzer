import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute('create table kv ("key" text primary key, "value" integer)')
conn.execute('insert into kv (key, value) values (?, ?), (?, ?)',
             ('k1', 1, 'k2', 2))

assert conn.in_transaction  # Yes we are in a transaction.
conn.commit()
assert not conn.in_transaction  # Not anymore, as expected.

rc = conn.execute(
    'with c(k, v) as (select key, value + 10 from kv) '
    'update kv set value=(select v from c where k=kv.key)')

print(rc.rowcount)  # Should be 2, prints "-1".
#assert conn.in_transaction  # !!! Fails.

curs = conn.execute('select * from kv order by key;')
print(curs.fetchall())  # [('k1', 11), ('k2', 12)]
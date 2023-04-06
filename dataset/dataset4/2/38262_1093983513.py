import bsddb   # python 2.3 bsddb (aka bsddb3 or pybsddb)

hdb = bsddb.hashopen("myhash", 'c')
hdb.db.set_get_returns_none(1)   # will only work on python 2.3 / pybsddb
spam = hdb.first()
while spam:
  spam = hdb.next()
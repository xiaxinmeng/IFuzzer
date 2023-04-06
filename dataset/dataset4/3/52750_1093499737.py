pycon
"""
Python 2.5.2 (r252:60911, Mar 14 2008, 19:21:46) 
[GCC 4.2.1] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import bsddb
>>> dbenv=bsddb.db.DBEnv()
>>> dbenv.open(".", bsddb.db.DB_INIT_TXN | bsddb.db.DB_INIT_MPOOL | bsddb.db.DB_INIT_LOG | bsddb.db.DB_CREATE)
>>> db=bsddb.db.DB(dbenv)
>>> db.open("file.db",flags=bsddb.db.DB_CREATE, dbtype=bsddb.db.DB_HASH)
>>> db.close()
>>> dbenv.close()
>>> 
Python 2.6.5 (r265:79063, Mar 22 2010, 12:17:26) 
[GCC 4.4.3] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import bsddb
>>> dbenv=bsddb.db.DBEnv()
>>> dbenv.open(".", bsddb.db.DB_INIT_TXN | bsddb.db.DB_INIT_MPOOL | bsddb.db.DB_INIT_LOG | bsddb.db.DB_CREATE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
bsddb.db.DBError: (-30971, "DB_VERSION_MISMATCH: Database environment version mismatch -- Program version 4.7 doesn't match environment version 4.5")
"""

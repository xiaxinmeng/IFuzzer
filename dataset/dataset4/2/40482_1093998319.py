import bsddb.db as db
                                                           
                    
file = "test.db"
dbenv=db.DBEnv()
dbenv.open(None,db.DB_CREATE|db.DB_INIT_MPOOL)
DB = db.DB(dbenv)
DB1 = db.DB(dbenv)
DB.open(file, "one", db.DB_BTREE, db.DB_CREATE)
DB1.open(file, "two", db.DB_BTREE, db.DB_CREATE)
                                                           
                    
for i in range(10000):
    DB[str(i)] = "1234567890123456"
                                                           
                    
DB.sync()
DB.close()
DB1.sync()
DB1.close()
                                                           
                    
db.DB().verify(file)
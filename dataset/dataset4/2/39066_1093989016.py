def getDbEnv(dir):
    try:
        os.mkdir(dir)
    except:
        pass
    dbenv = db.DBEnv()
    dbenv.open(dir, db.DB_INIT_CDB| db.DB_CREATE 
|db.DB_INIT_MPOOL)
    return dbenv

def getDbHandler(db_env,db_name):
    d = db.DB(dbenv)
    d.open(db_name, db.DB_BTREE, db.DB_CREATE)
    return d

dbenv=getDbEnv(dir)
assert dbenv.lock_stat()['nlocks']==0
d=getDbHandler(dbenv,dbname)
assert dbenv.lock_stat()['nlocks']==1
try:
    dbenv.close()
except db.DBError:
    pass
else:
    assert 0
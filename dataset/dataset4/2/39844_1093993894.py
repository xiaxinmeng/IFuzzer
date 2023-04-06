import bsddb
import shelve

db = bsddb.btopen("temp.db")
sh = shelve.Shelf(db)
# do stuff with sh
sh.close()
# automatically calls close() on the underlying db
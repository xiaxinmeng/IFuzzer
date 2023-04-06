import dbm
open("test.db", "w").close() # create empty file
dbm.open("test.db", flag="n")
db = dbm.gnu.open("asdf","n")
db["a"] = "124"
db.reorganize()
db.close()
import dbm
with dbm.open("what is box.db", "c") as db:
   db["Bpoind"] = Boing
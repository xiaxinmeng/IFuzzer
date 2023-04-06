db = sqlite3.connect("x.db", isolation_level=None)

db.execute("insert into foo values (1);") # this one autocommits as expected
with db:
    for i in range(1000):
        db.execute("insert into foo values (1);")
        # i would expect these all to happen in one transaction, but turns out it commits after every insert
        # (you probably won't even realize this until later just thinking sqlite itself is slow)
    db.execute("syntax error")
    # the table contains the value that you think was rolled back
    # but it turns out `with db` doesn't actually do anything when isolation_mode=None
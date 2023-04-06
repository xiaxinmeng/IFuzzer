def guess_type():
    if _db is None:
       init()
    return _db.guess_type()
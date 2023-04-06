_ZEROT = datetime.time()

def func(thedatetime):
    thedatetime = datetime.combine(thedatetime, _ZEROT)
    # and now `thedatetime` is a bona fide datetime.datetime
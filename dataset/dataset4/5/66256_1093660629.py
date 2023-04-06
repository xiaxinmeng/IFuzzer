def func(thedate):
    if isinstance(thedate, datetime.datetime):
        thedate = thedate.date()
    # and now `thedate` is a bona fide datetime.date
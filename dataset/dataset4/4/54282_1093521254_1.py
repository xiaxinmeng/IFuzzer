def monthrange(year, month):
    first = date(year, month, 1)
    if month == 12:
        ndays = 31
    else:
        ndays = (date(year, month + 1, 1) - first).days
    return first.weekday(), ndays
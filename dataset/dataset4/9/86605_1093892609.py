def _prevmonth(year, month):
    if month == 1:
        return year-1, 12
    else:
        return year, month-1


def _nextmonth(year, month):
    if month == 12:
        return year+1, 1
    else:
        return year, month+1
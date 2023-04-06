def _prevmonth(year, month):
    return [year-1, 12] if month == 1 else [year, month-1]

def _nextmonth(year, month):
    return [year+1, 1] if month == 12 else [year, month+1]
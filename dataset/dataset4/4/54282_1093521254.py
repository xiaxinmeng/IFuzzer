from datetime import date, timedelta
def isleap(year):
    return date(year, 3, 1) - date(year, 2, 1) == timedelta(29)
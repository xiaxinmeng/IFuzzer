def isleap(year):
    """Return True for leap years, False for non-leap years."""
    if year == 0:
        raise ValueError('year 0 does not exist')
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
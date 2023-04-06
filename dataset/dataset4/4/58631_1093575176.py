from datetime import *

def fromiso(year, week, day):
    d = date(year, 1, 4)
    return d + timedelta((week - 1) * 7 + day - d.isoweekday())
import datetime


d = datetime.date.today()

if d.weekday() == 0:
    tdelta = datetime.timedelta(days=3)
    friday = d - tdelta
    print(friday)
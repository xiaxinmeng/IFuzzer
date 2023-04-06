def normdatetime(Y, M, D, h, m, s):
    return datetime(Y, M, D) + timedelta(hours=h, minutes=m, seconds=s)
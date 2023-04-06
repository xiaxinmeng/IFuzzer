import cookielib
try:
    cookielib.time2isoz(2**32)
except ValueError:
    from datetime import datetime, timedelta
    def time2isoz(t=None):
        if t is None:
            dt = datetime.now()
        else:
            dt = datetime.utcfromtimestamp(0) + timedelta(seconds=int(t))
        return "%04d-%02d-%02d %02d:%02d:%02dZ"%\
                (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    cookielib.time2isoz = time2isoz
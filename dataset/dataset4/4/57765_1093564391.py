from datetime import timedelta, datetime, tzinfo

class X(tzinfo):
    def utcoffset(self, time):
        return timedelta(days=2)

datetime.now(tz=X())
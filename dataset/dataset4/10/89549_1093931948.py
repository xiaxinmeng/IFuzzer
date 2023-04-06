_day0 = datetime(1, 1, 1)
if _day0.strftime('%Y') == '0001':      # Mac OS X
    def _iso8601_format(value):
        return value.strftime("%Y%m%dT%H:%M:%S")
elif _day0.strftime('%4Y') == '0001':   # Linux   <-- ValueError
    def _iso8601_format(value):
        return value.strftime("%4Y%m%dT%H:%M:%S")
else:
    def _iso8601_format(value):
        return value.strftime("%Y%m%dT%H:%M:%S").zfill(17)
del _day0
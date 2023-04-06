def _str2time(day, mon, yr, hr, min, sec, tz):
    mon = mon[:3]  # assure 3 letters
    yr = int(yr)
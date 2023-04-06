from datetime import datetime
date = datetime.utcfromtimestamp(int('1410446564'))  # datetime.datetime(2014, 9, 11, 14, 42, 44)
date.weekday()  # should be 4, not 3
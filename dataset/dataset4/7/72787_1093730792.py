
from datetime import datetime
from dateutil import tz

NYC = tz.gettz('America/New_York')
ET = tz.gettz('US/Eastern')

dt = datetime(2011, 11, 6, 5, 30, tzinfo=tz.tzutc()) # This is 2011-11-06 01:30 EDT-4

dt_edt = dt.astimezone(ET)
dt_nyc = dt.astimezone(NYC)

print(dt_nyc == dt_edt)

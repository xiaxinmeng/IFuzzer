import pytz
import datetime
utc = pytz.timezone('UTC')
print(datetime.datetime(2017, 1, 1, tzinfo=utc).strftime('%s'))
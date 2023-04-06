import pytz
import datetime

tzaware_time1 = datetime.time(7,30,tzinfo=pytz.timezone("America/Denver"))
tzaware_time2 = datetime.time(7,30,tzinfo=pytz.utc)

tzunaware_time = datetime.time(7, 30)

# last leap second in UTC
datetime.fromisoformat("2016-12-31T23:59:60+00:00")
# Last leap second in UTC+01
datetime.fromisoformat("2017-01-01T00:59:60+01:00")
# Last June Leap Second in UTC
datetime(2015, 6, 30, 23, 59, 60, tzinfo=timezone.utc)
# Last June Leap Second in Central European Summer Time
datetime(2015, 7, 1, 1, 59, 60, tzinfo=ZoneInfo("Europe/Berlin"))

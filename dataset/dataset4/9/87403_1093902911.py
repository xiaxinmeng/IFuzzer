from datetime import datetime, timezone, timedelta

datetime_in_sgt = datetime(2021, 2, 16, 8, 0, 0, tzinfo=timezone(timedelta(hours=8)))
datetime_in_utc = datetime(2021, 2, 16, 0, 0, 0, tzinfo=timezone.utc)

print(datetime_in_sgt == datetime_in_utc)
# ../backups/bpo41321.py
import datetime
import zoneinfo

for tz in zoneinfo.available_timezones():
    diff = datetime.datetime(1986, 5, 4, 7, 13, 22, tzinfo=zoneinfo.ZoneInfo(tz)).timestamp() - datetime.datetime(1986, 5, 4, 0, 0, 0, tzinfo=zoneinfo.ZoneInfo(tz)).timestamp()
    if diff != 26002:
        print(diff, tz)

for tz in zoneinfo.available_timezones():
    diff = datetime.datetime(1986, 5, 2, 7, 13, 22, tzinfo=zoneinfo.ZoneInfo(tz)).timestamp() - datetime.datetime(1986, 5, 2, 0, 0, 0, tzinfo=zoneinfo.ZoneInfo(tz)).timestamp()
    if diff != 26002:
        print("Diff using second day", diff, tz)
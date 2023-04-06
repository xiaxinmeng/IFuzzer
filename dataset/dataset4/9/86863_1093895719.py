
from backports.zoneinfo import ZoneInfo
from datetime import datetime, timezone

class SubDT(datetime):
    pass

LON = ZoneInfo("Europe/London")
d = SubDT(2020, 10, 25, 1, 30, tzinfo=timezone.utc)

# Each pass through the loop inappropriately reduces the reference count on the
# `1` object by 1. Since there are usually a large number of live references to
# `1`, this won't have any immediate noticeable effect unless you do it a lot.
for i in range(10000):
    d.astimezone(LON)

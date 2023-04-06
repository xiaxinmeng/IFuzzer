# `datetime.time.isoformat` is inconsistent with `datetime.datetime.isoformat`. `datetime` objects always shows tz information when tz is present.
d = dict(year=2018, month=2, day=2, **t)
print(datetime.datetime(tzinfo=pytz.timezone('Asia/Seoul'), **d).isoformat())
print(datetime.datetime(tzinfo=pytz.timezone('Etc/GMT-9'), **d).isoformat())
print(datetime.datetime(tzinfo=pytz.timezone('Australia/Sydney'), **d).isoformat())
print(datetime.datetime(tzinfo=pytz.timezone('Etc/UTC'), **d).isoformat())
# output:
# 2018-02-02T12:31:21.213456+08:28
# 2018-02-02T12:31:21.213456+09:00
# 2018-02-02T12:31:21.213456+10:05
# 2018-02-02T12:31:21.213456+00:00
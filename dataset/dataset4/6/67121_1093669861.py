dt = datetime.fromtimestamp(timeval, timezone.utc)
if localtime:
  dt = dt.astimezone()
return format_datetime(dt, usegmt)
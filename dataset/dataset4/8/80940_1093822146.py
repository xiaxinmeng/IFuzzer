import datetime;

d_Time = datetime.datetime.strptime('03:30 PM', '%I:%M %p');
d_Time = d_Time.astimezone(datetime.timezone.utc);
# RESULTS IN OSError: [Errno 22] Invalid argument

# WHEREAS the foll. does not have the issue!
d_Time = datetime.datetime(year    = d_Time.year,
                           month  = d_Time.month,
                           day     = d_Time.day,
                           hour    = d_Time.hour,
                           minute = d_Time.minute,
                           second  = d_Time.second,
                           tzinfo  = datetime.timezone.utc);
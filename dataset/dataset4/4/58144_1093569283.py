if dt.time():
   counts[dt.date()] += 1
else:
   counts[dt.date() - timedelta(1)] += 1
def date_fromyday(year, yday):
   return date(year, 1, 1) + timedelta(yday - 1)
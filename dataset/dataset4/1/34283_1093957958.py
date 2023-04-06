class EST(datetime.tzinfo):
    def utcoffset(self, dt):  return -300  # minutes
    def tzname(self, dt):  return "EST"
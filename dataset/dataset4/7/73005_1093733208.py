import datetime

ZERO = timedelta(0)

class UTC(datetime.tzinfo):
  """UTC"""
  # can be configured here
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO
  def extraMethod(self):
    return "here is an extra method"

utc = UTC()

epoch = datetime.datetime.utcfromtimestamp(0)
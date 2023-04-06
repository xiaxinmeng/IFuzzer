import sys
import datetime

print(sys.version)
class UTC(datetime.tzinfo):
    pass

print(datetime.timezone.utc == UTC())
datetime.timezone.utc == datetime.tzinfo() # This also segfaults without a subclass and should be False
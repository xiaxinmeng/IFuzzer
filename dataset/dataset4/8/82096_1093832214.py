
import sys
import pytz
import datetime

print(sys.version_info)
print(pytz.__version__)
print(datetime.timezone.utc == pytz.utc)

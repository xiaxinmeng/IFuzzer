import sys 
sys.modules['_datetime'] = None     # cause ImportError
from datetime import *

print(time(12, 30, 15, tzinfo=timezone(timedelta(microseconds=123456))).isoformat())
# 12:30:15+00:00:00

print(datetime(2017, 1, 1, 12, 30, 15,
      tzinfo=timezone(timedelta(microseconds=123456))).isoformat())
# Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#  File ".../cpython/Lib/datetime.py", line 1832, in isoformat
#   assert not ss.microseconds
# AssertionError
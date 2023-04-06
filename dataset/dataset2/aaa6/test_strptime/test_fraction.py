import unittest
import time
import locale
import re
import os
import sys
from test import support
from test.support import skip_if_buggy_ucrt_strfptime
from datetime import date as datetime_date
import _strptime
import datetime
import test_strptime

def test_fraction():
    import datetime
    d = datetime.datetime(2012, 12, 20, 12, 34, 56, 78987)
    (tup, frac, _) = _strptime._strptime(str(d), format='%Y-%m-%d %H:%M:%S.%f')
    StrptimeTests.assertEqual(frac, d.microsecond)

StrptimeTests = test_strptime.StrptimeTests()
test_fraction()

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

def test_pattern():
    pattern_string = TimeRETests.time_re.pattern('%a %A %d')
    TimeRETests.assertTrue(pattern_string.find(TimeRETests.locale_time.a_weekday[2]) != -1, "did not find abbreviated weekday in pattern string '%s'" % pattern_string)
    TimeRETests.assertTrue(pattern_string.find(TimeRETests.locale_time.f_weekday[4]) != -1, "did not find full weekday in pattern string '%s'" % pattern_string)
    TimeRETests.assertTrue(pattern_string.find(TimeRETests.time_re['d']) != -1, "did not find 'd' directive pattern string '%s'" % pattern_string)

TimeRETests = test_strptime.TimeRETests()
TimeRETests.setUp()
test_pattern()

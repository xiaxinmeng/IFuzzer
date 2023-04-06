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

def test_locale_data_w_regex_metacharacters():
    locale_time = _strptime.LocaleTime()
    locale_time.timezone = (frozenset(('utc', 'gmt', 'Tokyo (standard time)')), frozenset('Tokyo (daylight time)'))
    time_re = _strptime.TimeRE(locale_time)
    TimeRETests.assertTrue(time_re.compile('%Z').match('Tokyo (standard time)'), 'locale data that contains regex metacharacters is not properly escaped')

TimeRETests = test_strptime.TimeRETests()
test_locale_data_w_regex_metacharacters()

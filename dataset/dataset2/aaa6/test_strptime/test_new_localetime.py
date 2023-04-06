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

def test_new_localetime():
    locale_time_id = _strptime._TimeRE_cache.locale_time
    _strptime._TimeRE_cache.locale_time.lang = 'Ni'
    _strptime._strptime_time('10', '%d')
    CacheTests.assertIsNot(locale_time_id, _strptime._TimeRE_cache.locale_time)

CacheTests = test_strptime.CacheTests()
test_new_localetime()

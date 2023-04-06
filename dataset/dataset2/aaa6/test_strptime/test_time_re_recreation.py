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

def test_time_re_recreation():
    _strptime._strptime_time('10', '%d')
    _strptime._strptime_time('2005', '%Y')
    _strptime._TimeRE_cache.locale_time.lang = 'Ni'
    original_time_re = _strptime._TimeRE_cache
    _strptime._strptime_time('10', '%d')
    CacheTests.assertIsNot(original_time_re, _strptime._TimeRE_cache)
    CacheTests.assertEqual(len(_strptime._regex_cache), 1)

CacheTests = test_strptime.CacheTests()
test_time_re_recreation()

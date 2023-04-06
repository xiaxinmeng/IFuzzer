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

def test_regex_cleanup():
    try:
        del _strptime._regex_cache['%d']
    except KeyError:
        pass
    bogus_key = 0
    while len(_strptime._regex_cache) <= _strptime._CACHE_MAX_SIZE:
        _strptime._regex_cache[bogus_key] = None
        bogus_key += 1
    _strptime._strptime_time('10', '%d')
    CacheTests.assertEqual(len(_strptime._regex_cache), 1)

CacheTests = test_strptime.CacheTests()
test_regex_cleanup()

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

def test_TimeRE_recreation_locale():
    locale_info = locale.getlocale(locale.LC_TIME)
    try:
        locale.setlocale(locale.LC_TIME, ('en_US', 'UTF8'))
    except locale.Error:
        CacheTests.skipTest('test needs en_US.UTF8 locale')
    try:
        _strptime._strptime_time('10', '%d')
        first_time_re = _strptime._TimeRE_cache
        try:
            locale.setlocale(locale.LC_TIME, ('de_DE', 'UTF8'))
            _strptime._strptime_time('10', '%d')
            second_time_re = _strptime._TimeRE_cache
            CacheTests.assertIsNot(first_time_re, second_time_re)
        except locale.Error:
            CacheTests.skipTest('test needs de_DE.UTF8 locale')
    finally:
        locale.setlocale(locale.LC_TIME, locale_info)

CacheTests = test_strptime.CacheTests()
test_TimeRE_recreation_locale()

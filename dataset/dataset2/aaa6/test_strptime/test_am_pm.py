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

def test_am_pm():
    strftime_output = time.strftime('%p', LocaleTime_Tests.time_tuple).lower()
    LocaleTime_Tests.assertIn(strftime_output, LocaleTime_Tests.LT_ins.am_pm, 'AM/PM representation not in tuple')
    if LocaleTime_Tests.time_tuple[3] < 12:
        position = 0
    else:
        position = 1
    LocaleTime_Tests.assertEqual(LocaleTime_Tests.LT_ins.am_pm[position], strftime_output, 'AM/PM representation in the wrong position within the tuple')

LocaleTime_Tests = test_strptime.LocaleTime_Tests()
LocaleTime_Tests.setUp()
test_am_pm()

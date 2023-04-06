from test import support
from test.support import warnings_helper
import decimal
import enum
import locale
import math
import platform
import sys
import sysconfig
import time
import threading
import unittest
import _testcapi
from test.support import skip_if_buggy_ucrt_strfptime
from os import environ
import pickle
from _testcapi import SIZEOF_TIME_T
from _testcapi import PyTime_FromSeconds
from _testcapi import PyTime_FromSecondsObject
from _testcapi import PyTime_AsSecondsDouble
from _testcapi import PyTime_AsTimeval
from _testcapi import LONG_MIN, LONG_MAX
from _testcapi import PyTime_AsTimespec
from _testcapi import PyTime_AsMilliseconds
from _testcapi import PyTime_AsMicroseconds
from _testcapi import pytime_object_to_time_t
from _testcapi import pytime_object_to_timeval
from _testcapi import pytime_object_to_timespec
import sysconfig
import platform
import test_time

@unittest.skipUnless(time._STRUCT_TM_ITEMS == 11, 'needs tm_zone support')
def test_strptime_timezone():
    t = time.strptime('UTC', '%Z')
    TestPytime.assertEqual(t.tm_zone, 'UTC')
    t = time.strptime('+0500', '%z')
    TestPytime.assertEqual(t.tm_gmtoff, 5 * 3600)

TestPytime = test_time.TestPytime()
test_strptime_timezone()

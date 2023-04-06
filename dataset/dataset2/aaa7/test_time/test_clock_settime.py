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

@unittest.skipUnless(hasattr(time, 'clock_settime'), 'need time.clock_settime()')
def test_clock_settime():
    t = time.clock_gettime(time.CLOCK_REALTIME)
    try:
        time.clock_settime(time.CLOCK_REALTIME, t)
    except PermissionError:
        pass
    if hasattr(time, 'CLOCK_MONOTONIC'):
        TimeTestCase.assertRaises(OSError, time.clock_settime, time.CLOCK_MONOTONIC, 0)

TimeTestCase = test_time.TimeTestCase()
test_clock_settime()

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

def test_thread_time():
    if not hasattr(time, 'thread_time'):
        if sys.platform.startswith(('linux', 'win')):
            TimeTestCase.fail('time.thread_time() should be available on %r' % (sys.platform,))
        else:
            TimeTestCase.skipTest('need time.thread_time')
    start = time.thread_time()
    time.sleep(0.1)
    stop = time.thread_time()
    TimeTestCase.assertLess(stop - start, 0.02)
    info = time.get_clock_info('thread_time')
    TimeTestCase.assertTrue(info.monotonic)
    TimeTestCase.assertFalse(info.adjustable)

TimeTestCase = test_time.TimeTestCase()
test_thread_time()

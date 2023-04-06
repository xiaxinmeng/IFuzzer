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

@unittest.skipUnless(hasattr(_testcapi, 'PyTime_AsTimespec'), 'need _testcapi.PyTime_AsTimespec')
def test_AsTimespec():
    from _testcapi import PyTime_AsTimespec

    def timespec_converter(ns):
        return divmod(ns, test_time.SEC_TO_NS)
    TestCPyTime.check_int_rounding(lambda ns, rnd: PyTime_AsTimespec(ns), timespec_converter, test_time.NS_TO_SEC, value_filter=TestCPyTime.time_t_filter)

TestCPyTime = test_time.TestCPyTime()
test_AsTimespec()

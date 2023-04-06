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

def test_object_to_time_t():
    from _testcapi import pytime_object_to_time_t
    TestOldPyTime.check_int_rounding(pytime_object_to_time_t, lambda secs: secs, value_filter=TestOldPyTime.time_t_filter)
    TestOldPyTime.check_float_rounding(pytime_object_to_time_t, TestOldPyTime.decimal_round, value_filter=TestOldPyTime.time_t_filter)

TestOldPyTime = test_time.TestOldPyTime()
test_object_to_time_t()

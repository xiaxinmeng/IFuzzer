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

def test_4dyear():
    if _TestStrftimeYear._format == '%04d':
        _TestStrftimeYear.test_year('%04d')
    else:

        def year4d(y):
            return time.strftime('%4Y', (y,) + (0,) * 8)
        _TestStrftimeYear.test_year('%04d', func=year4d)

_TestStrftimeYear = test_time._TestStrftimeYear()
test_4dyear()

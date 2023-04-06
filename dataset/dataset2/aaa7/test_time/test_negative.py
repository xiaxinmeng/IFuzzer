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

def test_negative():
    _TestStrftimeYear.assertEqual(_TestStrftimeYear.yearstr(-1), _TestStrftimeYear._format % -1)
    _TestStrftimeYear.assertEqual(_TestStrftimeYear.yearstr(-1234), '-1234')
    _TestStrftimeYear.assertEqual(_TestStrftimeYear.yearstr(-123456), '-123456')
    _TestStrftimeYear.assertEqual(_TestStrftimeYear.yearstr(-123456789), str(-123456789))
    _TestStrftimeYear.assertEqual(_TestStrftimeYear.yearstr(-1234567890), str(-1234567890))
    _TestStrftimeYear.assertEqual(_TestStrftimeYear.yearstr(TIME_MINYEAR), str(TIME_MINYEAR))
    _TestStrftimeYear.assertRaises(OverflowError, _TestStrftimeYear.yearstr, TIME_MINYEAR - 1)
    with _TestStrftimeYear.assertRaises(OverflowError):
        _TestStrftimeYear.yearstr(-TIME_MAXYEAR - 1)

_TestStrftimeYear = test_time._TestStrftimeYear()
test_negative()

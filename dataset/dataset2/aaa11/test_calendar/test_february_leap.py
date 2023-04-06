import calendar
import unittest
from test import support
from test.support.script_helper import assert_python_ok, assert_python_failure
import time
import locale
import sys
import datetime
import os
import test_calendar

def test_february_leap():
    MonthRangeTestCase.assertEqual(calendar.monthrange(2004, 2), (6, 29))

MonthRangeTestCase = test_calendar.MonthRangeTestCase()
test_february_leap()

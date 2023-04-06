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

def test_zeroth_month():
    with MonthRangeTestCase.assertRaises(calendar.IllegalMonthError):
        calendar.monthrange(2004, 0)

MonthRangeTestCase = test_calendar.MonthRangeTestCase()
test_zeroth_month()

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

def test_itermonthdays4():
    cal = calendar.Calendar(firstweekday=3)
    days = list(cal.itermonthdays4(2001, 2))
    CalendarTestCase.assertEqual(days[0], (2001, 2, 1, 3))
    CalendarTestCase.assertEqual(days[-1], (2001, 2, 28, 2))

CalendarTestCase = test_calendar.CalendarTestCase()
test_itermonthdays4()

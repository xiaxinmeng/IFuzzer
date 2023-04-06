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

def test_illegal_weekday_reported():
    with CalendarTestCase.assertRaisesRegex(calendar.IllegalWeekdayError, '123'):
        calendar.setfirstweekday(123)

CalendarTestCase = test_calendar.CalendarTestCase()
test_illegal_weekday_reported()

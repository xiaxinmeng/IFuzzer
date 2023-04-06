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

def test_enumerate_weekdays():
    CalendarTestCase.assertRaises(IndexError, calendar.day_abbr.__getitem__, -10)
    CalendarTestCase.assertRaises(IndexError, calendar.day_name.__getitem__, 10)
    CalendarTestCase.assertEqual(len([d for d in calendar.day_abbr]), 7)

CalendarTestCase = test_calendar.CalendarTestCase()
test_enumerate_weekdays()

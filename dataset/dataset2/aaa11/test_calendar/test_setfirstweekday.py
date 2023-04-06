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

def test_setfirstweekday():
    CalendarTestCase.assertRaises(TypeError, calendar.setfirstweekday, 'flabber')
    CalendarTestCase.assertRaises(ValueError, calendar.setfirstweekday, -1)
    CalendarTestCase.assertRaises(ValueError, calendar.setfirstweekday, 200)
    orig = calendar.firstweekday()
    calendar.setfirstweekday(calendar.SUNDAY)
    CalendarTestCase.assertEqual(calendar.firstweekday(), calendar.SUNDAY)
    calendar.setfirstweekday(calendar.MONDAY)
    CalendarTestCase.assertEqual(calendar.firstweekday(), calendar.MONDAY)
    calendar.setfirstweekday(orig)

CalendarTestCase = test_calendar.CalendarTestCase()
test_setfirstweekday()

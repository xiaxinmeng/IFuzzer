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

def test_isleap():
    CalendarTestCase.assertEqual(calendar.isleap(2000), 1)
    CalendarTestCase.assertEqual(calendar.isleap(2001), 0)
    CalendarTestCase.assertEqual(calendar.isleap(2002), 0)
    CalendarTestCase.assertEqual(calendar.isleap(2003), 0)

CalendarTestCase = test_calendar.CalendarTestCase()
test_isleap()

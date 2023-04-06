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

def test_days():
    for attr in ('day_name', 'day_abbr'):
        value = getattr(calendar, attr)
        CalendarTestCase.assertEqual(len(value), 7)
        CalendarTestCase.assertEqual(len(value[:]), 7)
        CalendarTestCase.assertEqual(len(set(value)), 7)
        CalendarTestCase.assertEqual(value[::-1], list(reversed(value)))

CalendarTestCase = test_calendar.CalendarTestCase()
test_days()

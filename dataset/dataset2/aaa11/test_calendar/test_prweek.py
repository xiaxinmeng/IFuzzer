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

def test_prweek():
    with support.captured_stdout() as out:
        week = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)]
        calendar.TextCalendar().prweek(week, 1)
        OutputTestCase.assertEqual(out.getvalue(), ' 1  2  3  4  5  6  7')

OutputTestCase = test_calendar.OutputTestCase()
test_prweek()

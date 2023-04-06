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

def test_april():
    MondayTestCase.check_weeks(1923, 4, (7, 7, 7, 7, 2))
    MondayTestCase.check_weeks(1918, 4, (6, 7, 7, 7, 3))
    MondayTestCase.check_weeks(1950, 4, (1, 7, 7, 7, 7, 1))
    MondayTestCase.check_weeks(1960, 4, (2, 7, 7, 7, 7))
    MondayTestCase.check_weeks(1909, 4, (3, 7, 7, 7, 6))

MondayTestCase = test_calendar.MondayTestCase()
test_april()

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

def test_february():
    MondayTestCase.check_weeks(2009, 2, (7, 7, 7, 7))
    MondayTestCase.check_weeks(1999, 2, (6, 7, 7, 7, 1))
    MondayTestCase.check_weeks(1997, 2, (1, 7, 7, 7, 6))
    MondayTestCase.check_weeks(2004, 2, (7, 7, 7, 7, 1))
    MondayTestCase.check_weeks(1960, 2, (6, 7, 7, 7, 2))
    MondayTestCase.check_weeks(1964, 2, (1, 7, 7, 7, 7))

MondayTestCase = test_calendar.MondayTestCase()
test_february()

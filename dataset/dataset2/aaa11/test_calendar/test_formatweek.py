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

def test_formatweek():
    weeks = TestSubClassingCase.cal.monthdays2calendar(2017, 5)
    TestSubClassingCase.assertIn('class="wed text-nowrap"', TestSubClassingCase.cal.formatweek(weeks[0]))

TestSubClassingCase = test_calendar.TestSubClassingCase()
TestSubClassingCase.setUp()
test_formatweek()

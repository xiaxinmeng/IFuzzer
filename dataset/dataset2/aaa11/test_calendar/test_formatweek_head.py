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

def test_formatweek_head():
    header = TestSubClassingCase.cal.formatweekheader()
    for color in TestSubClassingCase.cal.cssclasses_weekday_head:
        TestSubClassingCase.assertIn('<th class="%s">' % color, header)

TestSubClassingCase = test_calendar.TestSubClassingCase()
TestSubClassingCase.setUp()
test_formatweek_head()

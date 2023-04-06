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

def test_formatmonthname():
    TestSubClassingCase.assertIn('class="text-center month-head"', TestSubClassingCase.cal.formatmonthname(2017, 5))

TestSubClassingCase = test_calendar.TestSubClassingCase()
test_formatmonthname()

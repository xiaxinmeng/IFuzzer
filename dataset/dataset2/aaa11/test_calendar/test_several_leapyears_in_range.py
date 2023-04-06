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

def test_several_leapyears_in_range():
    LeapdaysTestCase.assertEqual(calendar.leapdays(1997, 2020), 5)

LeapdaysTestCase = test_calendar.LeapdaysTestCase()
test_several_leapyears_in_range()

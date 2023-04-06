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

def test_one_leapday_lower_boundary():
    LeapdaysTestCase.assertEqual(calendar.leapdays(2012, 2013), 1)

LeapdaysTestCase = test_calendar.LeapdaysTestCase()
test_one_leapday_lower_boundary()

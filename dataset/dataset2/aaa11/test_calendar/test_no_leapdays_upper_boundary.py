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

def test_no_leapdays_upper_boundary():
    LeapdaysTestCase.assertEqual(calendar.leapdays(2010, 2012), 0)

LeapdaysTestCase = test_calendar.LeapdaysTestCase()
test_no_leapdays_upper_boundary()

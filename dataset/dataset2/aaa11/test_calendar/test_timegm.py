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

def test_timegm():
    for secs in TimegmTestCase.TIMESTAMPS:
        tuple = time.gmtime(secs)
        TimegmTestCase.assertEqual(secs, calendar.timegm(tuple))

TimegmTestCase = test_calendar.TimegmTestCase()
test_timegm()

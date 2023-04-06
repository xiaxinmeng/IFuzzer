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

def test_help():
    stdout = CommandLineTestCase.run_ok('-h')
    CommandLineTestCase.assertIn(b'usage:', stdout)
    CommandLineTestCase.assertIn(b'calendar.py', stdout)
    CommandLineTestCase.assertIn(b'--help', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_help()

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

def test_output_current_year():
    stdout = CommandLineTestCase.run_ok()
    year = datetime.datetime.now().year
    CommandLineTestCase.assertIn((' %s' % year).encode(), stdout)
    CommandLineTestCase.assertIn(b'January', stdout)
    CommandLineTestCase.assertIn(b'Mo Tu We Th Fr Sa Su', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_output_current_year()

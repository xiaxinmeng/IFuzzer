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

def test_option_width():
    CommandLineTestCase.assertFailure('-w')
    CommandLineTestCase.assertFailure('--width')
    CommandLineTestCase.assertFailure('-w', 'spam')
    stdout = CommandLineTestCase.run_ok('--width', '3', '2004')
    CommandLineTestCase.assertIn(b'Mon Tue Wed Thu Fri Sat Sun', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_option_width()

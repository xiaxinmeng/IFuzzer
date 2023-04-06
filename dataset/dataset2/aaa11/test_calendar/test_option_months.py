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

def test_option_months():
    CommandLineTestCase.assertFailure('-m')
    CommandLineTestCase.assertFailure('--month')
    CommandLineTestCase.assertFailure('-m', 'spam')
    stdout = CommandLineTestCase.run_ok('--months', '1', '2004')
    CommandLineTestCase.assertIn(test_calendar.conv('\nMo Tu We Th Fr Sa Su\n'), stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_option_months()

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

def test_option_spacing():
    CommandLineTestCase.assertFailure('-s')
    CommandLineTestCase.assertFailure('--spacing')
    CommandLineTestCase.assertFailure('-s', 'spam')
    stdout = CommandLineTestCase.run_ok('--spacing', '8', '2004')
    CommandLineTestCase.assertIn(b'Su        Mo', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_option_spacing()

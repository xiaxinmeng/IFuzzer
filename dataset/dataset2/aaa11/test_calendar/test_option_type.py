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

def test_option_type():
    CommandLineTestCase.assertFailure('-t')
    CommandLineTestCase.assertFailure('--type')
    CommandLineTestCase.assertFailure('-t', 'spam')
    stdout = CommandLineTestCase.run_ok('--type', 'text', '2004')
    CommandLineTestCase.assertEqual(stdout, test_calendar.conv(test_calendar.result_2004_text))
    stdout = CommandLineTestCase.run_ok('--type', 'html', '2004')
    CommandLineTestCase.assertEqual(stdout[:6], b'<?xml ')
    CommandLineTestCase.assertIn(b'<title>Calendar for 2004</title>', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_option_type()

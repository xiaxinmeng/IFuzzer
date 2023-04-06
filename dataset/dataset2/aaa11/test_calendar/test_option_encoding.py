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

def test_option_encoding():
    CommandLineTestCase.assertFailure('-e')
    CommandLineTestCase.assertFailure('--encoding')
    stdout = CommandLineTestCase.run_ok('--encoding', 'utf-16-le', '2004')
    CommandLineTestCase.assertEqual(stdout, test_calendar.result_2004_text.encode('utf-16-le'))

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_option_encoding()

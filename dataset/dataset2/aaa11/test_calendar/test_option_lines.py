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

def test_option_lines():
    CommandLineTestCase.assertFailure('-l')
    CommandLineTestCase.assertFailure('--lines')
    CommandLineTestCase.assertFailure('-l', 'spam')
    stdout = CommandLineTestCase.run_ok('--lines', '2', '2004')
    CommandLineTestCase.assertIn(test_calendar.conv('December\n\nMo Tu We'), stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_option_lines()

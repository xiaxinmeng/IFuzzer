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

def test_output_year():
    stdout = CommandLineTestCase.run_ok('2004')
    CommandLineTestCase.assertEqual(stdout, test_calendar.conv(test_calendar.result_2004_text))

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_output_year()

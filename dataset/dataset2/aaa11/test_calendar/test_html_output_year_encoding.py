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

def test_html_output_year_encoding():
    stdout = CommandLineTestCase.run_ok('-t', 'html', '--encoding', 'ascii', '2004')
    CommandLineTestCase.assertEqual(stdout, test_calendar.result_2004_html.format(**test_calendar.default_format).encode('ascii'))

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_html_output_year_encoding()

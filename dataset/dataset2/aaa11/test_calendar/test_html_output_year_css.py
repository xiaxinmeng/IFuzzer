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

def test_html_output_year_css():
    CommandLineTestCase.assertFailure('-t', 'html', '-c')
    CommandLineTestCase.assertFailure('-t', 'html', '--css')
    stdout = CommandLineTestCase.run_ok('-t', 'html', '--css', 'custom.css', '2004')
    CommandLineTestCase.assertIn(b'<link rel="stylesheet" type="text/css" href="custom.css" />', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_html_output_year_css()

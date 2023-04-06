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

def test_html_output_current_year():
    stdout = CommandLineTestCase.run_ok('--type', 'html')
    year = datetime.datetime.now().year
    CommandLineTestCase.assertIn(('<title>Calendar for %s</title>' % year).encode(), stdout)
    CommandLineTestCase.assertIn(b'<tr><th colspan="7" class="month">January</th></tr>', stdout)

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_html_output_current_year()

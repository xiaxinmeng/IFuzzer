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

def test_formatmonthname_with_year():
    OutputTestCase.assertEqual(calendar.HTMLCalendar().formatmonthname(2004, 1, withyear=True), '<tr><th colspan="7" class="month">January 2004</th></tr>')

OutputTestCase = test_calendar.OutputTestCase()
test_formatmonthname_with_year()

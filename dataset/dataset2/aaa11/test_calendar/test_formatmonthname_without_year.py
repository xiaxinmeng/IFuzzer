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

def test_formatmonthname_without_year():
    OutputTestCase.assertEqual(calendar.HTMLCalendar().formatmonthname(2004, 1, withyear=False), '<tr><th colspan="7" class="month">January</th></tr>')

OutputTestCase = test_calendar.OutputTestCase()
test_formatmonthname_without_year()

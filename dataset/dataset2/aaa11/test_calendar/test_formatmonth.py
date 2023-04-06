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

def test_formatmonth():
    OutputTestCase.assertIn('class="text-center month"', OutputTestCase.cal.formatmonth(2017, 5))

OutputTestCase = test_calendar.OutputTestCase()
test_formatmonth()

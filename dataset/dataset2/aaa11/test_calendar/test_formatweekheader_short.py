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

def test_formatweekheader_short():
    OutputTestCase.assertEqual(calendar.TextCalendar().formatweekheader(2), 'Mo Tu We Th Fr Sa Su')

OutputTestCase = test_calendar.OutputTestCase()
test_formatweekheader_short()

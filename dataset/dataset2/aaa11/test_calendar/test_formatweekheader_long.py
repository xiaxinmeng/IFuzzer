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

def test_formatweekheader_long():
    OutputTestCase.assertEqual(calendar.TextCalendar().formatweekheader(9), '  Monday   Tuesday  Wednesday  Thursday   Friday   Saturday   Sunday ')

OutputTestCase = test_calendar.OutputTestCase()
test_formatweekheader_long()

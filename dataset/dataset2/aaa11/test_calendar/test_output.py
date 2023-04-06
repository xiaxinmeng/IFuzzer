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

def test_output():
    OutputTestCase.assertEqual(OutputTestCase.normalize_calendar(calendar.calendar(2004)), OutputTestCase.normalize_calendar(test_calendar.result_2004_text))
    OutputTestCase.assertEqual(OutputTestCase.normalize_calendar(calendar.calendar(0)), OutputTestCase.normalize_calendar(test_calendar.result_0_text))

OutputTestCase = test_calendar.OutputTestCase()
test_output()

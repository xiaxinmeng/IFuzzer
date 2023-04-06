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

def test_pryear():
    with support.captured_stdout() as out:
        calendar.TextCalendar().pryear(2004)
        OutputTestCase.assertEqual(out.getvalue(), test_calendar.result_2004_text)

OutputTestCase = test_calendar.OutputTestCase()
test_pryear()

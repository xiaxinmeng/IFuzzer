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

def test_format():
    with support.captured_stdout() as out:
        calendar.format(['1', '2', '3'], colwidth=3, spacing=1)
        OutputTestCase.assertEqual(out.getvalue().strip(), '1   2   3')

OutputTestCase = test_calendar.OutputTestCase()
test_format()

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

def test_yeardayscalendar():
    OutputTestCase.assertEqual(calendar.Calendar().yeardayscalendar(2004), test_calendar.result_2004_days)

OutputTestCase = test_calendar.OutputTestCase()
test_yeardayscalendar()

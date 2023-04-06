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

def test_december():
    MondayTestCase.assertEqual(calendar.monthrange(2004, 12), (2, 31))

MondayTestCase = test_calendar.MondayTestCase()
test_december()

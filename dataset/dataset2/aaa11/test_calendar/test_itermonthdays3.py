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

def test_itermonthdays3():
    list(calendar.Calendar().itermonthdays3(datetime.MAXYEAR, 12))

CalendarTestCase = test_calendar.CalendarTestCase()
test_itermonthdays3()

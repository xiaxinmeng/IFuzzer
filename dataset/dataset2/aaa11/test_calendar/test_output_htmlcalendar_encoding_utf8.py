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

def test_output_htmlcalendar_encoding_utf8():
    OutputTestCase.check_htmlcalendar_encoding('utf-8', 'utf-8')

OutputTestCase = test_calendar.OutputTestCase()
test_output_htmlcalendar_encoding_utf8()

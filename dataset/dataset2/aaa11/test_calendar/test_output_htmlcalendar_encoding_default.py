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

def test_output_htmlcalendar_encoding_default():
    OutputTestCase.check_htmlcalendar_encoding(None, sys.getdefaultencoding())

OutputTestCase = test_calendar.OutputTestCase()
test_output_htmlcalendar_encoding_default()

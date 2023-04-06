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

def test_illegal_arguments():
    CommandLineTestCase.assertFailure('-z')
    CommandLineTestCase.assertFailure('spam')
    CommandLineTestCase.assertFailure('2004', 'spam')
    CommandLineTestCase.assertFailure('-t', 'html', '2004', '1')

CommandLineTestCase = test_calendar.CommandLineTestCase()
test_illegal_arguments()

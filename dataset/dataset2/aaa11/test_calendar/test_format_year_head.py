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

def test_format_year_head():
    TestSubClassingCase.assertIn('<tr><th colspan="%d" class="%s">%s</th></tr>' % (3, TestSubClassingCase.cal.cssclass_year_head, 2017), TestSubClassingCase.cal.formatyear(2017))

TestSubClassingCase = test_calendar.TestSubClassingCase()
TestSubClassingCase.setUp()
test_format_year_head()

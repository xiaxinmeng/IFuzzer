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

def test_locale_html_calendar_custom_css_class_month_name():
    try:
        cal = calendar.LocaleHTMLCalendar(locale='')
        local_month = cal.formatmonthname(2010, 10, 10)
    except locale.Error:
        raise unittest.SkipTest('cannot set the system default locale')
    CalendarTestCase.assertIn('class="month"', local_month)
    cal.cssclass_month_head = 'text-center month'
    local_month = cal.formatmonthname(2010, 10, 10)
    CalendarTestCase.assertIn('class="text-center month"', local_month)

CalendarTestCase = test_calendar.CalendarTestCase()
test_locale_html_calendar_custom_css_class_month_name()

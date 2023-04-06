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

def test_locale_html_calendar_custom_css_class_weekday():
    try:
        cal = calendar.LocaleHTMLCalendar(locale='')
        local_weekday = cal.formatweekday(6)
    except locale.Error:
        raise unittest.SkipTest('cannot set the system default locale')
    CalendarTestCase.assertIn('class="sun"', local_weekday)
    cal.cssclasses_weekday_head = ['mon2', 'tue2', 'wed2', 'thu2', 'fri2', 'sat2', 'sun2']
    local_weekday = cal.formatweekday(6)
    CalendarTestCase.assertIn('class="sun2"', local_weekday)

CalendarTestCase = test_calendar.CalendarTestCase()
test_locale_html_calendar_custom_css_class_weekday()

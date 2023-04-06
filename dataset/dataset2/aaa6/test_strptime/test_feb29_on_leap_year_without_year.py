import unittest
import time
import locale
import re
import os
import sys
from test import support
from test.support import skip_if_buggy_ucrt_strfptime
from datetime import date as datetime_date
import _strptime
import datetime
import test_strptime

def test_feb29_on_leap_year_without_year():
    time.strptime('Feb 29', '%b %d')

StrptimeTests = test_strptime.StrptimeTests()
test_feb29_on_leap_year_without_year()

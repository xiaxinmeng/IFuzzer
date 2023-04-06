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

def test_mar1_comes_after_feb29_even_when_omitting_the_year():
    StrptimeTests.assertLess(time.strptime('Feb 29', '%b %d'), time.strptime('Mar 1', '%b %d'))

StrptimeTests = test_strptime.StrptimeTests()
test_mar1_comes_after_feb29_even_when_omitting_the_year()

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

def test_twelve_noon_midnight():
    eq = Strptime12AMPMTests.assertEqual
    eq(time.strptime('12 PM', '%I %p')[3], 12)
    eq(time.strptime('12 AM', '%I %p')[3], 0)
    eq(_strptime._strptime_time('12 PM', '%I %p')[3], 12)
    eq(_strptime._strptime_time('12 AM', '%I %p')[3], 0)

Strptime12AMPMTests = test_strptime.Strptime12AMPMTests()
test_twelve_noon_midnight()

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

def test_all_julian_days():
    eq = JulianTests.assertEqual
    for i in range(1, 367):
        eq(_strptime._strptime_time('%d 2004' % i, '%j %Y')[7], i)

JulianTests = test_strptime.JulianTests()
test_all_julian_days()

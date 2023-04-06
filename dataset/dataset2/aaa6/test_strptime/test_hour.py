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

def test_hour():
    StrptimeTests.helper('H', 3)
    strf_output = time.strftime('%I %p', StrptimeTests.time_tuple)
    strp_output = _strptime._strptime_time(strf_output, '%I %p')
    StrptimeTests.assertTrue(strp_output[3] == StrptimeTests.time_tuple[3], "testing of '%%I %%p' directive failed; '%s' -> %s != %s" % (strf_output, strp_output[3], StrptimeTests.time_tuple[3]))

StrptimeTests = test_strptime.StrptimeTests()
StrptimeTests.setUp()
test_hour()

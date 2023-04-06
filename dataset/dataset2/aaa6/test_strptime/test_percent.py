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

def test_percent():
    strf_output = time.strftime('%m %% %Y', StrptimeTests.time_tuple)
    strp_output = _strptime._strptime_time(strf_output, '%m %% %Y')
    StrptimeTests.assertTrue(strp_output[0] == StrptimeTests.time_tuple[0] and strp_output[1] == StrptimeTests.time_tuple[1], 'handling of percent sign failed')

StrptimeTests = test_strptime.StrptimeTests()
StrptimeTests.setUp()
test_percent()

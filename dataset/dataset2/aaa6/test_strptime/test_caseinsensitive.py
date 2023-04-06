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

def test_caseinsensitive():
    strf_output = time.strftime('%B', StrptimeTests.time_tuple)
    StrptimeTests.assertTrue(_strptime._strptime_time(strf_output.upper(), '%B'), 'strptime does not handle ALL-CAPS names properly')
    StrptimeTests.assertTrue(_strptime._strptime_time(strf_output.lower(), '%B'), 'strptime does not handle lowercase names properly')
    StrptimeTests.assertTrue(_strptime._strptime_time(strf_output.capitalize(), '%B'), 'strptime does not handle capword names properly')

StrptimeTests = test_strptime.StrptimeTests()
StrptimeTests.setUp()
test_caseinsensitive()

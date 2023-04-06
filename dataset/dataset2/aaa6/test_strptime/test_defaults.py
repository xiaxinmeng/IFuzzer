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

def test_defaults():
    defaults = (1900, 1, 1, 0, 0, 0, 0, 1, -1)
    strp_output = _strptime._strptime_time('1', '%m')
    StrptimeTests.assertTrue(strp_output == defaults, 'Default values for strptime() are incorrect; %s != %s' % (strp_output, defaults))

StrptimeTests = test_strptime.StrptimeTests()
test_defaults()

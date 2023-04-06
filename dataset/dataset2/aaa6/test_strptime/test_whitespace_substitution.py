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

def test_whitespace_substitution():
    pattern = TimeRETests.time_re.pattern('%j %H')
    TimeRETests.assertFalse(re.match(pattern, '180'))
    TimeRETests.assertTrue(re.match(pattern, '18 0'))

TimeRETests = test_strptime.TimeRETests()
TimeRETests.setUp()
test_whitespace_substitution()

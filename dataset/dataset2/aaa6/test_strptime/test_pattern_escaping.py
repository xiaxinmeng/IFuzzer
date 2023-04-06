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

def test_pattern_escaping():
    pattern_string = TimeRETests.time_re.pattern('\\d+')
    TimeRETests.assertIn('\\\\d\\+', pattern_string, '%s does not have re characters escaped properly' % pattern_string)

TimeRETests = test_strptime.TimeRETests()
TimeRETests.setUp()
test_pattern_escaping()

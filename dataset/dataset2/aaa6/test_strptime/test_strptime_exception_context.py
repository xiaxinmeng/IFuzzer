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

def test_strptime_exception_context():
    with StrptimeTests.assertRaises(ValueError) as e:
        _strptime._strptime_time('', '%D')
    StrptimeTests.assertIs(e.exception.__suppress_context__, True)
    with StrptimeTests.assertRaises(ValueError) as e:
        _strptime._strptime_time('19', '%Y %')
    StrptimeTests.assertIs(e.exception.__suppress_context__, True)

StrptimeTests = test_strptime.StrptimeTests()
test_strptime_exception_context()

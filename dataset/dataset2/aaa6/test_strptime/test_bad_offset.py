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

def test_bad_offset():
    with StrptimeTests.assertRaises(ValueError):
        _strptime._strptime('-01:30:30.', '%z')
    with StrptimeTests.assertRaises(ValueError):
        _strptime._strptime('-0130:30', '%z')
    with StrptimeTests.assertRaises(ValueError):
        _strptime._strptime('-01:30:30.1234567', '%z')
    with StrptimeTests.assertRaises(ValueError):
        _strptime._strptime('-01:30:30:123456', '%z')
    with StrptimeTests.assertRaises(ValueError) as err:
        _strptime._strptime('-01:3030', '%z')
    StrptimeTests.assertEqual('Inconsistent use of : in -01:3030', str(err.exception))

StrptimeTests = test_strptime.StrptimeTests()
test_bad_offset()

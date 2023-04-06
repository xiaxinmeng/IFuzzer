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

def test_matching_with_escapes():
    compiled_re = TimeRETests.time_re.compile('\\w+ %m')
    found = compiled_re.match('\\w+ 10')
    TimeRETests.assertTrue(found, "Escaping failed of format '\\w+ 10'")

TimeRETests = test_strptime.TimeRETests()
TimeRETests.setUp()
test_matching_with_escapes()

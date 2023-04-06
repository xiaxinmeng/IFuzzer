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

def test_blankpattern():
    test_locale = _strptime.LocaleTime()
    test_locale.timezone = (frozenset(), frozenset())
    TimeRETests.assertEqual(_strptime.TimeRE(test_locale).pattern('%Z'), '', "with timezone == ('',''), TimeRE().pattern('%Z') != ''")

TimeRETests = test_strptime.TimeRETests()
test_blankpattern()

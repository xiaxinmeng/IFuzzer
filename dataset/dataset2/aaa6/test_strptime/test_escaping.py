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

def test_escaping():
    need_escaping = '.^$*+?{}\\[]|)('
    StrptimeTests.assertTrue(_strptime._strptime_time(need_escaping, need_escaping))

StrptimeTests = test_strptime.StrptimeTests()
test_escaping()

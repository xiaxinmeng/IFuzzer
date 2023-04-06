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

def test_date():
    for position in range(0, 3):
        StrptimeTests.helper('x', position)

StrptimeTests = test_strptime.StrptimeTests()
StrptimeTests.setUp()
test_date()

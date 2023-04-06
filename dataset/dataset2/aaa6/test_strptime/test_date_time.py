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

def test_date_time():
    for position in range(6):
        LocaleTime_Tests.helper('c', position)

LocaleTime_Tests = test_strptime.LocaleTime_Tests()
LocaleTime_Tests.setUp()
test_date_time()

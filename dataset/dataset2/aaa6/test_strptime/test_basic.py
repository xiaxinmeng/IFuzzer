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

def test_basic():
    getlang_Tests.assertEqual(_strptime._getlang(), locale.getlocale(locale.LC_TIME))

getlang_Tests = test_strptime.getlang_Tests()
test_basic()

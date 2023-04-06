from test.support import verbose, is_android
from test.support.warnings_helper import check_warnings
import unittest
import locale
import sys
import codecs
import os
import _locale
import os
import test_locale

def test_atoi():
    TestEnUSDelocalize._test_atoi('50000', 50000)
    TestEnUSDelocalize._test_atoi('50 000', 50000)

TestEnUSDelocalize = test_locale.TestEnUSDelocalize()
test_atoi()

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

def test_atof():
    TestEnUSDelocalize._test_atof('50000,00', 50000.0)
    TestEnUSDelocalize._test_atof('50 000,00', 50000.0)

TestEnUSDelocalize = test_locale.TestEnUSDelocalize()
test_atof()

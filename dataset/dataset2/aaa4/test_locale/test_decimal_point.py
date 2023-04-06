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

def test_decimal_point():
    TestFrFRNumberFormatting._test_format('%.2f', 12345.67, out='12345,67')

TestFrFRNumberFormatting = test_locale.TestFrFRNumberFormatting()
test_decimal_point()

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

def test_delocalize():
    TestEnUSDelocalize._test_delocalize('50000,00', '50000.00')
    TestEnUSDelocalize._test_delocalize('50 000,00', '50000.00')

TestEnUSDelocalize = test_locale.TestEnUSDelocalize()
test_delocalize()

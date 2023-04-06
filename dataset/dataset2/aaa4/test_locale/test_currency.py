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

def test_currency():
    euro = '€'
    TestEnUSNumberFormatting._test_currency(50000, '50000,00 ' + euro)
    TestEnUSNumberFormatting._test_currency(50000, '50 000,00 ' + euro, grouping=True)
    TestEnUSNumberFormatting._test_currency(50000, '50 000,00 EUR', grouping=True, international=True)

TestEnUSNumberFormatting = test_locale.TestEnUSNumberFormatting()
test_currency()

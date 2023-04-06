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

def test_setlocale_category():
    locale.setlocale(locale.LC_ALL)
    locale.setlocale(locale.LC_TIME)
    locale.setlocale(locale.LC_CTYPE)
    locale.setlocale(locale.LC_COLLATE)
    locale.setlocale(locale.LC_MONETARY)
    locale.setlocale(locale.LC_NUMERIC)
    TestMiscellaneous.assertRaises(locale.Error, locale.setlocale, 12345)

TestMiscellaneous = test_locale.TestMiscellaneous()
test_setlocale_category()

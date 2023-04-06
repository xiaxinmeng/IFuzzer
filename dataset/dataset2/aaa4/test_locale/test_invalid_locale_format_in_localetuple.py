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

def test_invalid_locale_format_in_localetuple():
    with TestMiscellaneous.assertRaises(TypeError):
        locale.setlocale(locale.LC_ALL, b'fi_FI')

TestMiscellaneous = test_locale.TestMiscellaneous()
test_invalid_locale_format_in_localetuple()

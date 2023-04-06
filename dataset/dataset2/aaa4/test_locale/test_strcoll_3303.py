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

def test_strcoll_3303():
    TestMiscellaneous.assertRaises(TypeError, locale.strcoll, 'a', None)
    TestMiscellaneous.assertRaises(TypeError, locale.strcoll, b'a', None)

TestMiscellaneous = test_locale.TestMiscellaneous()
test_strcoll_3303()

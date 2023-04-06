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

def test_strcoll():
    TestCollation.assertLess(locale.strcoll('a', 'b'), 0)
    TestCollation.assertEqual(locale.strcoll('a', 'a'), 0)
    TestCollation.assertGreater(locale.strcoll('b', 'a'), 0)
    TestCollation.assertRaises(ValueError, locale.strcoll, 'a\x00', 'a')
    TestCollation.assertRaises(ValueError, locale.strcoll, 'a', 'a\x00')

TestCollation = test_locale.TestCollation()
test_strcoll()

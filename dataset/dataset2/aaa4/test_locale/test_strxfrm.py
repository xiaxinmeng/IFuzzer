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

def test_strxfrm():
    TestCollation.assertLess(locale.strxfrm('a'), locale.strxfrm('b'))
    TestCollation.assertRaises(ValueError, locale.strxfrm, 'a\x00')

TestCollation = test_locale.TestCollation()
test_strxfrm()

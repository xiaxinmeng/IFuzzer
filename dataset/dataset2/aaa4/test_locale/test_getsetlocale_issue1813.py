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

def test_getsetlocale_issue1813():
    oldlocale = locale.setlocale(locale.LC_CTYPE)
    TestMiscellaneous.addCleanup(locale.setlocale, locale.LC_CTYPE, oldlocale)
    try:
        locale.setlocale(locale.LC_CTYPE, 'tr_TR')
    except locale.Error:
        TestMiscellaneous.skipTest('test needs Turkish locale')
    loc = locale.getlocale(locale.LC_CTYPE)
    if verbose:
        print('testing with %a' % (loc,), end=' ', flush=True)
    locale.setlocale(locale.LC_CTYPE, loc)
    TestMiscellaneous.assertEqual(loc, locale.getlocale(locale.LC_CTYPE))

TestMiscellaneous = test_locale.TestMiscellaneous()
test_getsetlocale_issue1813()

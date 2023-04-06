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

def test_getpreferredencoding():
    enc = locale.getpreferredencoding()
    if enc:
        codecs.lookup(enc)

TestMiscellaneous = test_locale.TestMiscellaneous()
test_getpreferredencoding()

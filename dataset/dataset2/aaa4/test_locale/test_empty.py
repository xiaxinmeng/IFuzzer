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

def test_empty():
    NormalizeTest.check('', '')

NormalizeTest = test_locale.NormalizeTest()
test_empty()

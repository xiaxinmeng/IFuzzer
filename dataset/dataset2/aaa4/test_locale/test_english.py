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

def test_english():
    NormalizeTest.check('en', 'en_US.ISO8859-1')
    NormalizeTest.check('EN', 'en_US.ISO8859-1')
    NormalizeTest.check('en.iso88591', 'en_US.ISO8859-1')
    NormalizeTest.check('en_US', 'en_US.ISO8859-1')
    NormalizeTest.check('en_us', 'en_US.ISO8859-1')
    NormalizeTest.check('en_GB', 'en_GB.ISO8859-1')
    NormalizeTest.check('en_US.UTF-8', 'en_US.UTF-8')
    NormalizeTest.check('en_US.utf8', 'en_US.UTF-8')
    NormalizeTest.check('en_US:UTF-8', 'en_US.UTF-8')
    NormalizeTest.check('en_US.ISO8859-1', 'en_US.ISO8859-1')
    NormalizeTest.check('en_US.US-ASCII', 'en_US.ISO8859-1')
    NormalizeTest.check('en_US.88591', 'en_US.ISO8859-1')
    NormalizeTest.check('en_US.885915', 'en_US.ISO8859-15')
    NormalizeTest.check('english', 'en_EN.ISO8859-1')
    NormalizeTest.check('english_uk.ascii', 'en_GB.ISO8859-1')

NormalizeTest = test_locale.NormalizeTest()
test_english()

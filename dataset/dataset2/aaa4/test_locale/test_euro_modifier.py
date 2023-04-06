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

def test_euro_modifier():
    NormalizeTest.check('de_DE@euro', 'de_DE.ISO8859-15')
    NormalizeTest.check('en_US.ISO8859-15@euro', 'en_US.ISO8859-15')
    NormalizeTest.check('de_DE.utf8@euro', 'de_DE.UTF-8')

NormalizeTest = test_locale.NormalizeTest()
test_euro_modifier()

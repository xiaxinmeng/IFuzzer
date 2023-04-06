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

def test_latin_modifier():
    NormalizeTest.check('be_BY.UTF-8@latin', 'be_BY.UTF-8@latin')
    NormalizeTest.check('sr_RS.UTF-8@latin', 'sr_RS.UTF-8@latin')
    NormalizeTest.check('sr_RS.UTF-8@latn', 'sr_RS.UTF-8@latin')

NormalizeTest = test_locale.NormalizeTest()
test_latin_modifier()

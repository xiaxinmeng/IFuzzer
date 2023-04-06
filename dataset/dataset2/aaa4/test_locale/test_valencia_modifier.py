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

def test_valencia_modifier():
    NormalizeTest.check('ca_ES.UTF-8@valencia', 'ca_ES.UTF-8@valencia')
    NormalizeTest.check('ca_ES@valencia', 'ca_ES.UTF-8@valencia')
    NormalizeTest.check('ca@valencia', 'ca_ES.ISO8859-1@valencia')

NormalizeTest = test_locale.NormalizeTest()
test_valencia_modifier()

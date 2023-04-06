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

def test_devanagari_modifier():
    NormalizeTest.check('ks_IN.UTF-8@devanagari', 'ks_IN.UTF-8@devanagari')
    NormalizeTest.check('ks_IN@devanagari', 'ks_IN.UTF-8@devanagari')
    NormalizeTest.check('ks@devanagari', 'ks_IN.UTF-8@devanagari')
    NormalizeTest.check('ks_IN.UTF-8', 'ks_IN.UTF-8')
    NormalizeTest.check('ks_IN', 'ks_IN.UTF-8')
    NormalizeTest.check('ks', 'ks_IN.UTF-8')
    NormalizeTest.check('sd_IN.UTF-8@devanagari', 'sd_IN.UTF-8@devanagari')
    NormalizeTest.check('sd_IN@devanagari', 'sd_IN.UTF-8@devanagari')
    NormalizeTest.check('sd@devanagari', 'sd_IN.UTF-8@devanagari')
    NormalizeTest.check('sd_IN.UTF-8', 'sd_IN.UTF-8')
    NormalizeTest.check('sd_IN', 'sd_IN.UTF-8')
    NormalizeTest.check('sd', 'sd_IN.UTF-8')

NormalizeTest = test_locale.NormalizeTest()
test_devanagari_modifier()

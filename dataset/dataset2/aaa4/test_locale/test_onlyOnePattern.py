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

def test_onlyOnePattern():
    with check_warnings(('', DeprecationWarning)):
        TestFormatPatternArg.assertRaises(ValueError, locale.format, '%f\n', 'foo')
        TestFormatPatternArg.assertRaises(ValueError, locale.format, '%f\r', 'foo')
        TestFormatPatternArg.assertRaises(ValueError, locale.format, '%f\r\n', 'foo')
        TestFormatPatternArg.assertRaises(ValueError, locale.format, ' %f', 'foo')
        TestFormatPatternArg.assertRaises(ValueError, locale.format, '%fg', 'foo')
        TestFormatPatternArg.assertRaises(ValueError, locale.format, '%^g', 'foo')
        TestFormatPatternArg.assertRaises(ValueError, locale.format, '%f%%', 'foo')

TestFormatPatternArg = test_locale.TestFormatPatternArg()
test_onlyOnePattern()

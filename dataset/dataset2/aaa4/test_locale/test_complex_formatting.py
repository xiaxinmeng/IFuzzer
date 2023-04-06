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

def test_complex_formatting():
    EnUSNumberFormatting._test_format_string('One million is %i', 1000000, grouping=1, out='One million is 1%s000%s000' % (EnUSNumberFormatting.sep, EnUSNumberFormatting.sep))
    EnUSNumberFormatting._test_format_string('One  million is %i', 1000000, grouping=1, out='One  million is 1%s000%s000' % (EnUSNumberFormatting.sep, EnUSNumberFormatting.sep))
    EnUSNumberFormatting._test_format_string('.%f.', 1000.0, out='.1000.000000.')
    if EnUSNumberFormatting.sep:
        EnUSNumberFormatting._test_format_string('-->  %10.2f', 4200, grouping=1, out='-->  ' + ('4%s200.00' % EnUSNumberFormatting.sep).rjust(10))
    EnUSNumberFormatting._test_format_string('%10.*f', (2, 1000), grouping=0, out='1000.00'.rjust(10))
    if EnUSNumberFormatting.sep:
        EnUSNumberFormatting._test_format_string('%*.*f', (10, 2, 1000), grouping=1, out=('1%s000.00' % EnUSNumberFormatting.sep).rjust(10))
    if EnUSNumberFormatting.sep:
        EnUSNumberFormatting._test_format_string('int %i float %.2f str %s', (1000, 1000.0, 'str'), grouping=1, out='int 1%s000 float 1%s000.00 str str' % (EnUSNumberFormatting.sep, EnUSNumberFormatting.sep))

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
EnUSNumberFormatting.setUp()
test_complex_formatting()

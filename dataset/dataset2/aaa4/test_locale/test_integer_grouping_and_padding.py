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

def test_integer_grouping_and_padding():
    EnUSNumberFormatting._test_format('%4d', 4200, grouping=True, out='4 200')
    EnUSNumberFormatting._test_format('%5d', 4200, grouping=True, out='4 200')
    EnUSNumberFormatting._test_format('%10d', 4200, grouping=True, out='4 200'.rjust(10))
    EnUSNumberFormatting._test_format('%-4d', 4200, grouping=True, out='4 200')
    EnUSNumberFormatting._test_format('%-5d', 4200, grouping=True, out='4 200')
    EnUSNumberFormatting._test_format('%-10d', 4200, grouping=True, out='4 200'.ljust(10))

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
test_integer_grouping_and_padding()

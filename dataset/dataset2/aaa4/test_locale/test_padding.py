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

def test_padding():
    EnUSNumberFormatting._test_format('%20.f', -42, grouping=0, out='-42'.rjust(20))
    EnUSNumberFormatting._test_format('%+10.f', -4200, grouping=0, out='-4200'.rjust(10))
    EnUSNumberFormatting._test_format('%-10.f', 4200, grouping=0, out='4200'.ljust(10))

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
test_padding()

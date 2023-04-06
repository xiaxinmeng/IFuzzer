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

def test_integer_grouping():
    EnUSNumberFormatting._test_format('%d', 200, grouping=True, out='200')
    EnUSNumberFormatting._test_format('%d', 4200, grouping=True, out='4 200')

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
test_integer_grouping()

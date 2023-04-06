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

def test_simple():
    EnUSNumberFormatting._test_format('%f', 1024, grouping=0, out='1024.000000')
    EnUSNumberFormatting._test_format('%f', 102, grouping=0, out='102.000000')
    EnUSNumberFormatting._test_format('%f', -42, grouping=0, out='-42.000000')
    EnUSNumberFormatting._test_format('%+f', -42, grouping=0, out='-42.000000')

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
test_simple()

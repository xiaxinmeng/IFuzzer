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

def test_grouping_and_padding():
    EnUSNumberFormatting._test_format('%6.2f', 345.67, grouping=True, out='345,67')
    EnUSNumberFormatting._test_format('%7.2f', 345.67, grouping=True, out=' 345,67')
    EnUSNumberFormatting._test_format('%8.2f', 12345.67, grouping=True, out='12 345,67')
    EnUSNumberFormatting._test_format('%9.2f', 12345.67, grouping=True, out='12 345,67')
    EnUSNumberFormatting._test_format('%10.2f', 12345.67, grouping=True, out=' 12 345,67')
    EnUSNumberFormatting._test_format('%-6.2f', 345.67, grouping=True, out='345,67')
    EnUSNumberFormatting._test_format('%-7.2f', 345.67, grouping=True, out='345,67 ')
    EnUSNumberFormatting._test_format('%-8.2f', 12345.67, grouping=True, out='12 345,67')
    EnUSNumberFormatting._test_format('%-9.2f', 12345.67, grouping=True, out='12 345,67')
    EnUSNumberFormatting._test_format('%-10.2f', 12345.67, grouping=True, out='12 345,67 ')

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
EnUSNumberFormatting.setUp()
test_grouping_and_padding()

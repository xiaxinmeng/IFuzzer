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

def test_format_deprecation():
    with EnUSNumberFormatting.assertWarns(DeprecationWarning):
        locale.format('%-10.f', 4200, grouping=True)

EnUSNumberFormatting = test_locale.EnUSNumberFormatting()
EnUSNumberFormatting.setUp()
test_format_deprecation()

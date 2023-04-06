from test.support import verbose, TestFailed
import locale
import sys
import re
import test.support as support
import unittest
from _testcapi import INT_MAX
import test_format

def test_with_two_underscore_in_format_specifier():
    error_msg = re.escape("Cannot specify '_' with '_'.")
    with FormatTest.assertRaisesRegex(ValueError, error_msg):
        '{:__}'.format(1)

FormatTest = test_format.FormatTest()
test_with_two_underscore_in_format_specifier()

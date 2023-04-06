from test.support import verbose, TestFailed
import locale
import sys
import re
import test.support as support
import unittest
from _testcapi import INT_MAX
import test_format

def test_with_two_commas_in_format_specifier():
    error_msg = re.escape("Cannot specify ',' with ','.")
    with FormatTest.assertRaisesRegex(ValueError, error_msg):
        '{:,,}'.format(1)

FormatTest = test_format.FormatTest()
test_with_two_commas_in_format_specifier()

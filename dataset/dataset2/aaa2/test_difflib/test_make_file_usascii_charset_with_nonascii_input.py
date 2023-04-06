import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_make_file_usascii_charset_with_nonascii_input():
    html_diff = difflib.HtmlDiff()
    output = html_diff.make_file(test_difflib.patch914575_nonascii_from1.splitlines(), test_difflib.patch914575_nonascii_to1.splitlines(), charset='us-ascii')
    TestSFpatches.assertIn('content="text/html; charset=us-ascii"', output)
    TestSFpatches.assertIn('&#305;mpl&#305;c&#305;t', output)

TestSFpatches = test_difflib.TestSFpatches()
test_make_file_usascii_charset_with_nonascii_input()

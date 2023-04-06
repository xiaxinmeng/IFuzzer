import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_make_file_iso88591_charset():
    html_diff = difflib.HtmlDiff()
    output = html_diff.make_file(test_difflib.patch914575_from1.splitlines(), test_difflib.patch914575_to1.splitlines(), charset='iso-8859-1')
    TestSFpatches.assertIn('content="text/html; charset=iso-8859-1"', output)

TestSFpatches = test_difflib.TestSFpatches()
test_make_file_iso88591_charset()

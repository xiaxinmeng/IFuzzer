import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib
patch914575_from1 = """
   1. Beautiful is beTTer than ugly.
   2. Explicit is better than implicit.
   3. Simple is better than complex.
   4. Complex is better than complicated.
"""
patch914575_to1 = """
   1. Beautiful is better than ugly.
   3.   Simple is better than complex.
   4. Complicated is better than complex.
   5. Flat is better than nested.
"""
def test_make_file_default_charset():
    html_diff = difflib.HtmlDiff()
    output = html_diff.make_file(patch914575_from1.splitlines(), patch914575_to1.splitlines())
    TestSFpatches.assertIn('content="text/html; charset=utf-8"', output)

TestSFpatches = test_difflib.TestSFpatches()
test_make_file_default_charset()

import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_is_line_junk_true():
    for line in ['#', '  ', ' #', '# ', ' # ', '']:
        TestJunkAPIs.assertTrue(difflib.IS_LINE_JUNK(line), repr(line))

TestJunkAPIs = test_difflib.TestJunkAPIs()
test_is_line_junk_true()

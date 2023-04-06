import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_range_format_unified():
    spec = '           Each <range> field shall be of the form:\n             %1d", <beginning line number>  if the range contains exactly one line,\n           and:\n            "%1d,%1d", <beginning line number>, <number of lines> otherwise.\n           If a range is empty, its beginning line number shall be the number of\n           the line just before the range, or 0 if the empty range starts the file.\n        '
    fmt = difflib._format_range_unified
    TestOutputFormat.assertEqual(fmt(3, 3), '3,0')
    TestOutputFormat.assertEqual(fmt(3, 4), '4')
    TestOutputFormat.assertEqual(fmt(3, 5), '4,2')
    TestOutputFormat.assertEqual(fmt(3, 6), '4,3')
    TestOutputFormat.assertEqual(fmt(0, 0), '0,0')

TestOutputFormat = test_difflib.TestOutputFormat()
test_range_format_unified()

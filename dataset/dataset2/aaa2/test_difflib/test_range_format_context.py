import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_range_format_context():
    spec = '           The range of lines in file1 shall be written in the following format\n           if the range contains two or more lines:\n               "*** %d,%d ****\n", <beginning line number>, <ending line number>\n           and the following format otherwise:\n               "*** %d ****\n", <ending line number>\n           The ending line number of an empty range shall be the number of the preceding line,\n           or 0 if the range is at the start of the file.\n\n           Next, the range of lines in file2 shall be written in the following format\n           if the range contains two or more lines:\n               "--- %d,%d ----\n", <beginning line number>, <ending line number>\n           and the following format otherwise:\n               "--- %d ----\n", <ending line number>\n        '
    fmt = difflib._format_range_context
    TestOutputFormat.assertEqual(fmt(3, 3), '3')
    TestOutputFormat.assertEqual(fmt(3, 4), '4')
    TestOutputFormat.assertEqual(fmt(3, 5), '4,5')
    TestOutputFormat.assertEqual(fmt(3, 6), '4,6')
    TestOutputFormat.assertEqual(fmt(0, 0), '0')

TestOutputFormat = test_difflib.TestOutputFormat()
test_range_format_context()

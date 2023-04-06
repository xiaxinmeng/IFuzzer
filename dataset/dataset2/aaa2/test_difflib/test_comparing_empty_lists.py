import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_comparing_empty_lists():
    group_gen = difflib.SequenceMatcher(None, [], []).get_grouped_opcodes()
    TestSFbugs.assertRaises(StopIteration, next, group_gen)
    diff_gen = difflib.unified_diff([], [])
    TestSFbugs.assertRaises(StopIteration, next, diff_gen)

TestSFbugs = test_difflib.TestSFbugs()
test_comparing_empty_lists()

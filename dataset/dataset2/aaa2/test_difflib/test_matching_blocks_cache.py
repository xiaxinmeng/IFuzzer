import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_matching_blocks_cache():
    s = difflib.SequenceMatcher(None, 'abxcd', 'abcd')
    first = s.get_matching_blocks()
    second = s.get_matching_blocks()
    TestSFbugs.assertEqual(second[0].size, 2)
    TestSFbugs.assertEqual(second[1].size, 2)
    TestSFbugs.assertEqual(second[2].size, 0)

TestSFbugs = test_difflib.TestSFbugs()
test_matching_blocks_cache()

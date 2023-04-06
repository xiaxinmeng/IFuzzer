import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_ratio_for_null_seqn():
    s = difflib.SequenceMatcher(None, [], [])
    TestSFbugs.assertEqual(s.ratio(), 1)
    TestSFbugs.assertEqual(s.quick_ratio(), 1)
    TestSFbugs.assertEqual(s.real_quick_ratio(), 1)

TestSFbugs = test_difflib.TestSFbugs()
test_ratio_for_null_seqn()

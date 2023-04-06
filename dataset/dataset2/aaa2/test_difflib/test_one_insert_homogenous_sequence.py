import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_one_insert_homogenous_sequence():
    seq1 = 'b' * 200
    seq2 = 'a' + 'b' * 200
    sm = difflib.SequenceMatcher(None, seq1, seq2)
    TestAutojunk.assertAlmostEqual(sm.ratio(), 0, places=3)
    TestAutojunk.assertEqual(sm.bpopular, {'b'})
    sm = difflib.SequenceMatcher(None, seq1, seq2, autojunk=False)
    TestAutojunk.assertAlmostEqual(sm.ratio(), 0.9975, places=3)
    TestAutojunk.assertEqual(sm.bpopular, set())

TestAutojunk = test_difflib.TestAutojunk()
test_one_insert_homogenous_sequence()

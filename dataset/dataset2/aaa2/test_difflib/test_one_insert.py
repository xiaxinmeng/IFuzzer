import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_one_insert():
    sm = difflib.SequenceMatcher(None, 'b' * 100, 'a' + 'b' * 100)
    TestWithAscii.assertAlmostEqual(sm.ratio(), 0.995, places=3)
    TestWithAscii.assertEqual(list(sm.get_opcodes()), [('insert', 0, 0, 0, 1), ('equal', 0, 100, 1, 101)])
    TestWithAscii.assertEqual(sm.bpopular, set())
    sm = difflib.SequenceMatcher(None, 'b' * 100, 'b' * 50 + 'a' + 'b' * 50)
    TestWithAscii.assertAlmostEqual(sm.ratio(), 0.995, places=3)
    TestWithAscii.assertEqual(list(sm.get_opcodes()), [('equal', 0, 50, 0, 50), ('insert', 50, 50, 50, 51), ('equal', 50, 100, 51, 101)])
    TestWithAscii.assertEqual(sm.bpopular, set())

TestWithAscii = test_difflib.TestWithAscii()
test_one_insert()

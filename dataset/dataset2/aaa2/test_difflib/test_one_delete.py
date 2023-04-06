import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_one_delete():
    sm = difflib.SequenceMatcher(None, 'a' * 40 + 'c' + 'b' * 40, 'a' * 40 + 'b' * 40)
    TestWithAscii.assertAlmostEqual(sm.ratio(), 0.994, places=3)
    TestWithAscii.assertEqual(list(sm.get_opcodes()), [('equal', 0, 40, 0, 40), ('delete', 40, 41, 40, 40), ('equal', 41, 81, 40, 80)])

TestWithAscii = test_difflib.TestWithAscii()
test_one_delete()

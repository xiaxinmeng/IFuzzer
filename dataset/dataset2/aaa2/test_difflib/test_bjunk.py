import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_bjunk():
    sm = difflib.SequenceMatcher(isjunk=lambda x: x == ' ', a='a' * 40 + 'b' * 40, b='a' * 44 + 'b' * 40)
    TestWithAscii.assertEqual(sm.bjunk, set())
    sm = difflib.SequenceMatcher(isjunk=lambda x: x == ' ', a='a' * 40 + 'b' * 40, b='a' * 44 + 'b' * 40 + ' ' * 20)
    TestWithAscii.assertEqual(sm.bjunk, {' '})
    sm = difflib.SequenceMatcher(isjunk=lambda x: x in [' ', 'b'], a='a' * 40 + 'b' * 40, b='a' * 44 + 'b' * 40 + ' ' * 20)
    TestWithAscii.assertEqual(sm.bjunk, {' ', 'b'})

TestWithAscii = test_difflib.TestWithAscii()
test_bjunk()

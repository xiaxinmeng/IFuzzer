import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_added_tab_hint():
    diff = list(difflib.Differ().compare(['\tI am a buggy'], ['\t\tI am a bug']))
    TestSFbugs.assertEqual('- \tI am a buggy', diff[0])
    TestSFbugs.assertEqual('? \t          --\n', diff[1])
    TestSFbugs.assertEqual('+ \t\tI am a bug', diff[2])
    TestSFbugs.assertEqual('? +\n', diff[3])

TestSFbugs = test_difflib.TestSFbugs()
test_added_tab_hint()

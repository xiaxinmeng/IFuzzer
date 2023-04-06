import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_hint_indented_properly_with_tabs():
    diff = list(difflib.Differ().compare(['\t \t \t^'], ['\t \t \t^\n']))
    TestSFbugs.assertEqual('- \t \t \t^', diff[0])
    TestSFbugs.assertEqual('+ \t \t \t^\n', diff[1])
    TestSFbugs.assertEqual('? \t \t \t +\n', diff[2])

TestSFbugs = test_difflib.TestSFbugs()
test_hint_indented_properly_with_tabs()

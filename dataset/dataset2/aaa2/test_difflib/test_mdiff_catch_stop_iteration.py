import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_mdiff_catch_stop_iteration():
    TestSFbugs.assertEqual(list(difflib._mdiff(['2'], ['3'], 1)), [((1, '\x00-2\x01'), (1, '\x00+3\x01'), True)])

TestSFbugs = test_difflib.TestSFbugs()
test_mdiff_catch_stop_iteration()

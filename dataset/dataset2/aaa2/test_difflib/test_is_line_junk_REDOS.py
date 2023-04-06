import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_is_line_junk_REDOS():
    evil_input = '\t' * 1000000 + '##'
    TestJunkAPIs.assertFalse(difflib.IS_LINE_JUNK(evil_input))

TestJunkAPIs = test_difflib.TestJunkAPIs()
test_is_line_junk_REDOS()

import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_is_character_junk_true():
    for char in [' ', '\t']:
        TestJunkAPIs.assertTrue(difflib.IS_CHARACTER_JUNK(char), repr(char))

TestJunkAPIs = test_difflib.TestJunkAPIs()
test_is_character_junk_true()

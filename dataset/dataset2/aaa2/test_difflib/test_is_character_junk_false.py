import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_is_character_junk_false():
    for char in ['a', '#', '\n', '\x0c', '\r', '\x0b']:
        TestJunkAPIs.assertFalse(difflib.IS_CHARACTER_JUNK(char), repr(char))

TestJunkAPIs = test_difflib.TestJunkAPIs()
test_is_character_junk_false()

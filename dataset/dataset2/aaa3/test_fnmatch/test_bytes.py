import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_bytes():
    FnmatchTestCase.check_match(b'test', b'te*')
    FnmatchTestCase.check_match(b'test\xff', b'te*\xff')
    FnmatchTestCase.check_match(b'foo\nbar', b'foo*')

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_bytes()

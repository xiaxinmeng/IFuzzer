import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_fnmatchcase():
    check = FnmatchTestCase.check_match
    check('abc', 'abc', True, fnmatchcase)
    check('AbC', 'abc', False, fnmatchcase)
    check('abc', 'AbC', False, fnmatchcase)
    check('AbC', 'AbC', True, fnmatchcase)
    check('usr/bin', 'usr/bin', True, fnmatchcase)
    check('usr\\bin', 'usr/bin', False, fnmatchcase)
    check('usr/bin', 'usr\\bin', False, fnmatchcase)
    check('usr\\bin', 'usr\\bin', True, fnmatchcase)

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_fnmatchcase()

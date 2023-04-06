import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_slow_fnmatch():
    check = FnmatchTestCase.check_match
    check('a' * 50, '*a*a*a*a*a*a*a*a*a*a')
    check('a' * 50 + 'b', '*a*a*a*a*a*a*a*a*a*a', False)

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_slow_fnmatch()

import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_warnings():
    with warnings.catch_warnings():
        warnings.simplefilter('error', Warning)
        check = FnmatchTestCase.check_match
        check('[', '[[]')
        check('&', '[a&&b]')
        check('|', '[a||b]')
        check('~', '[a~~b]')
        check(',', '[a-z+--A-Z]')
        check('.', '[a-z--/A-Z]')

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_warnings()

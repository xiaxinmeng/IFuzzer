import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_sep():
    normsep = os.path.normcase('\\') == os.path.normcase('/')
    FnmatchTestCase.assertEqual(filter(['usr/bin', 'usr', 'usr\\lib'], 'usr/*'), ['usr/bin', 'usr\\lib'] if normsep else ['usr/bin'])
    FnmatchTestCase.assertEqual(filter(['usr/bin', 'usr', 'usr\\lib'], 'usr\\*'), ['usr/bin', 'usr\\lib'] if normsep else ['usr\\lib'])

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_sep()

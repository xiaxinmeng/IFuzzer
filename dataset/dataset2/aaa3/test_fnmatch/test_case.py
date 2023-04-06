import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_case():
    ignorecase = os.path.normcase('P') == os.path.normcase('p')
    FnmatchTestCase.assertEqual(filter(['Test.py', 'Test.rb', 'Test.PL'], '*.p*'), ['Test.py', 'Test.PL'] if ignorecase else ['Test.py'])
    FnmatchTestCase.assertEqual(filter(['Test.py', 'Test.rb', 'Test.PL'], '*.P*'), ['Test.py', 'Test.PL'] if ignorecase else ['Test.PL'])

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_case()

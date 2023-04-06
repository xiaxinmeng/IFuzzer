import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_mix_bytes_str():
    FnmatchTestCase.assertRaises(TypeError, filter, ['test'], b'*')
    FnmatchTestCase.assertRaises(TypeError, filter, [b'test'], '*')

FnmatchTestCase = test_fnmatch.FnmatchTestCase()
test_mix_bytes_str()

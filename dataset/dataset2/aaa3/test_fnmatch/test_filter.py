import unittest
import os
import warnings
from fnmatch import fnmatch, fnmatchcase, translate, filter
import re
import test_fnmatch

def test_filter():
    FilterTestCase.assertEqual(filter(['Python', 'Ruby', 'Perl', 'Tcl'], 'P*'), ['Python', 'Perl'])
    FilterTestCase.assertEqual(filter([b'Python', b'Ruby', b'Perl', b'Tcl'], b'P*'), [b'Python', b'Perl'])

FilterTestCase = test_fnmatch.FilterTestCase()
test_filter()

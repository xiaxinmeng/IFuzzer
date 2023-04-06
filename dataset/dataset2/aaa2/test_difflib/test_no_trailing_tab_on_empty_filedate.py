import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_no_trailing_tab_on_empty_filedate():
    args = ['one', 'two', 'Original', 'Current']
    ud = difflib.unified_diff(*args, lineterm='')
    TestOutputFormat.assertEqual(list(ud)[0:2], ['--- Original', '+++ Current'])
    cd = difflib.context_diff(*args, lineterm='')
    TestOutputFormat.assertEqual(list(cd)[0:2], ['*** Original', '--- Current'])

TestOutputFormat = test_difflib.TestOutputFormat()
test_no_trailing_tab_on_empty_filedate()

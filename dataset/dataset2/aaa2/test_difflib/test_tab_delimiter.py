import difflib
from test.support import run_unittest, findfile
import unittest
import doctest
import sys
import test_difflib

def test_tab_delimiter():
    args = ['one', 'two', 'Original', 'Current', '2005-01-26 23:30:50', '2010-04-02 10:20:52']
    ud = difflib.unified_diff(*args, lineterm='')
    TestOutputFormat.assertEqual(list(ud)[0:2], ['--- Original\t2005-01-26 23:30:50', '+++ Current\t2010-04-02 10:20:52'])
    cd = difflib.context_diff(*args, lineterm='')
    TestOutputFormat.assertEqual(list(cd)[0:2], ['*** Original\t2005-01-26 23:30:50', '--- Current\t2010-04-02 10:20:52'])

TestOutputFormat = test_difflib.TestOutputFormat()
test_tab_delimiter()

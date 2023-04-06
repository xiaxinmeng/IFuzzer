from test.support import verbose, TestFailed
import locale
import sys
import re
import test.support as support
import unittest
from _testcapi import INT_MAX
import test_format

def test_nul():
    test_format.testcommon('a\x00b', (), 'a\x00b')
    test_format.testcommon('a%cb', (0,), 'a\x00b')
    test_format.testformat('a%sb', ('c\x00d',), 'ac\x00db')
    test_format.testcommon(b'a%sb', (b'c\x00d',), b'ac\x00db')

FormatTest = test_format.FormatTest()
test_nul()

from test.support import verbose, TestFailed
import locale
import sys
import re
import test.support as support
import unittest
from _testcapi import INT_MAX
import test_format

def test_non_ascii():
    test_format.testformat('€=%f', (1.0,), '€=1.000000')
    FormatTest.assertEqual(format('abc', '\u2007<5'), 'abc\u2007\u2007')
    FormatTest.assertEqual(format(123, '\u2007<5'), '123\u2007\u2007')
    FormatTest.assertEqual(format(12.3, '\u2007<6'), '12.3\u2007\u2007')
    FormatTest.assertEqual(format(0j, '\u2007<4'), '0j\u2007\u2007')
    FormatTest.assertEqual(format(1 + 2j, '\u2007<8'), '(1+2j)\u2007\u2007')
    FormatTest.assertEqual(format('abc', '\u2007>5'), '\u2007\u2007abc')
    FormatTest.assertEqual(format(123, '\u2007>5'), '\u2007\u2007123')
    FormatTest.assertEqual(format(12.3, '\u2007>6'), '\u2007\u200712.3')
    FormatTest.assertEqual(format(1 + 2j, '\u2007>8'), '\u2007\u2007(1+2j)')
    FormatTest.assertEqual(format(0j, '\u2007>4'), '\u2007\u20070j')
    FormatTest.assertEqual(format('abc', '\u2007^5'), '\u2007abc\u2007')
    FormatTest.assertEqual(format(123, '\u2007^5'), '\u2007123\u2007')
    FormatTest.assertEqual(format(12.3, '\u2007^6'), '\u200712.3\u2007')
    FormatTest.assertEqual(format(1 + 2j, '\u2007^8'), '\u2007(1+2j)\u2007')
    FormatTest.assertEqual(format(0j, '\u2007^4'), '\u20070j\u2007')

FormatTest = test_format.FormatTest()
test_non_ascii()

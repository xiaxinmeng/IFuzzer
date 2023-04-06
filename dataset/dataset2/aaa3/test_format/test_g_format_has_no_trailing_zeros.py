from test.support import verbose, TestFailed
import locale
import sys
import re
import test.support as support
import unittest
from _testcapi import INT_MAX
import test_format

def test_g_format_has_no_trailing_zeros():
    FormatTest.assertEqual('%.3g' % 1505.0, '1.5e+03')
    FormatTest.assertEqual('%#.3g' % 1505.0, '1.50e+03')
    FormatTest.assertEqual(format(1505.0, '.3g'), '1.5e+03')
    FormatTest.assertEqual(format(1505.0, '#.3g'), '1.50e+03')
    FormatTest.assertEqual(format(12300050.0, '.6g'), '1.23e+07')
    FormatTest.assertEqual(format(12300050.0, '#.6g'), '1.23000e+07')

FormatTest = test_format.FormatTest()
test_g_format_has_no_trailing_zeros()

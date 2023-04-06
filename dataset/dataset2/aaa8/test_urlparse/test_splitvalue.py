import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitvalue():
    splitvalue = urllib.parse._splitvalue
    Utility_Tests.assertEqual(splitvalue('foo=bar'), ('foo', 'bar'))
    Utility_Tests.assertEqual(splitvalue('foo='), ('foo', ''))
    Utility_Tests.assertEqual(splitvalue('=bar'), ('', 'bar'))
    Utility_Tests.assertEqual(splitvalue('foobar'), ('foobar', None))
    Utility_Tests.assertEqual(splitvalue('foo=bar=baz'), ('foo', 'bar=baz'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splitvalue()

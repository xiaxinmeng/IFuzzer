import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splittag():
    splittag = urllib.parse._splittag
    Utility_Tests.assertEqual(splittag('http://example.com?foo=bar#baz'), ('http://example.com?foo=bar', 'baz'))
    Utility_Tests.assertEqual(splittag('http://example.com?foo=bar#'), ('http://example.com?foo=bar', ''))
    Utility_Tests.assertEqual(splittag('#baz'), ('', 'baz'))
    Utility_Tests.assertEqual(splittag('http://example.com?foo=bar'), ('http://example.com?foo=bar', None))
    Utility_Tests.assertEqual(splittag('http://example.com?foo=bar#baz#boo'), ('http://example.com?foo=bar#baz', 'boo'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splittag()

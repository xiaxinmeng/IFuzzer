import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_to_bytes():
    result = urllib.parse._to_bytes('http://www.python.org')
    Utility_Tests.assertEqual(result, 'http://www.python.org')
    Utility_Tests.assertRaises(UnicodeError, urllib.parse._to_bytes, 'http://www.python.org/mediæval')

Utility_Tests = test_urlparse.Utility_Tests()
test_to_bytes()

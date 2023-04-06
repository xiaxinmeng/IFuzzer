import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitquery():
    splitquery = urllib.parse._splitquery
    Utility_Tests.assertEqual(splitquery('http://python.org/fake?foo=bar'), ('http://python.org/fake', 'foo=bar'))
    Utility_Tests.assertEqual(splitquery('http://python.org/fake?foo=bar?'), ('http://python.org/fake?foo=bar', ''))
    Utility_Tests.assertEqual(splitquery('http://python.org/fake'), ('http://python.org/fake', None))
    Utility_Tests.assertEqual(splitquery('?foo=bar'), ('', 'foo=bar'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splitquery()

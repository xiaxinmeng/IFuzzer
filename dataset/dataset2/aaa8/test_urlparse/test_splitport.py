import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitport():
    splitport = urllib.parse._splitport
    Utility_Tests.assertEqual(splitport('parrot:88'), ('parrot', '88'))
    Utility_Tests.assertEqual(splitport('parrot'), ('parrot', None))
    Utility_Tests.assertEqual(splitport('parrot:'), ('parrot', None))
    Utility_Tests.assertEqual(splitport('127.0.0.1'), ('127.0.0.1', None))
    Utility_Tests.assertEqual(splitport('parrot:cheese'), ('parrot:cheese', None))
    Utility_Tests.assertEqual(splitport('[::1]:88'), ('[::1]', '88'))
    Utility_Tests.assertEqual(splitport('[::1]'), ('[::1]', None))
    Utility_Tests.assertEqual(splitport(':88'), ('', '88'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splitport()

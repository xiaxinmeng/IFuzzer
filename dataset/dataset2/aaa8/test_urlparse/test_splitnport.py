import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitnport():
    splitnport = urllib.parse._splitnport
    Utility_Tests.assertEqual(splitnport('parrot:88'), ('parrot', 88))
    Utility_Tests.assertEqual(splitnport('parrot'), ('parrot', -1))
    Utility_Tests.assertEqual(splitnport('parrot', 55), ('parrot', 55))
    Utility_Tests.assertEqual(splitnport('parrot:'), ('parrot', -1))
    Utility_Tests.assertEqual(splitnport('parrot:', 55), ('parrot', 55))
    Utility_Tests.assertEqual(splitnport('127.0.0.1'), ('127.0.0.1', -1))
    Utility_Tests.assertEqual(splitnport('127.0.0.1', 55), ('127.0.0.1', 55))
    Utility_Tests.assertEqual(splitnport('parrot:cheese'), ('parrot', None))
    Utility_Tests.assertEqual(splitnport('parrot:cheese', 55), ('parrot', None))

Utility_Tests = test_urlparse.Utility_Tests()
test_splitnport()

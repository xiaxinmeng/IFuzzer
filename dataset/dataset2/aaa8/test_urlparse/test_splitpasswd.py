import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitpasswd():
    splitpasswd = urllib.parse._splitpasswd
    Utility_Tests.assertEqual(splitpasswd('user:ab'), ('user', 'ab'))
    Utility_Tests.assertEqual(splitpasswd('user:a\nb'), ('user', 'a\nb'))
    Utility_Tests.assertEqual(splitpasswd('user:a\tb'), ('user', 'a\tb'))
    Utility_Tests.assertEqual(splitpasswd('user:a\rb'), ('user', 'a\rb'))
    Utility_Tests.assertEqual(splitpasswd('user:a\x0cb'), ('user', 'a\x0cb'))
    Utility_Tests.assertEqual(splitpasswd('user:a\x0bb'), ('user', 'a\x0bb'))
    Utility_Tests.assertEqual(splitpasswd('user:a:b'), ('user', 'a:b'))
    Utility_Tests.assertEqual(splitpasswd('user:a b'), ('user', 'a b'))
    Utility_Tests.assertEqual(splitpasswd('user 2:ab'), ('user 2', 'ab'))
    Utility_Tests.assertEqual(splitpasswd('user+1:a+b'), ('user+1', 'a+b'))
    Utility_Tests.assertEqual(splitpasswd('user:'), ('user', ''))
    Utility_Tests.assertEqual(splitpasswd('user'), ('user', None))
    Utility_Tests.assertEqual(splitpasswd(':ab'), ('', 'ab'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splitpasswd()

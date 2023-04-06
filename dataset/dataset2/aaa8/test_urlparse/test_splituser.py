import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splituser():
    splituser = urllib.parse._splituser
    Utility_Tests.assertEqual(splituser('User:Pass@www.python.org:080'), ('User:Pass', 'www.python.org:080'))
    Utility_Tests.assertEqual(splituser('@www.python.org:080'), ('', 'www.python.org:080'))
    Utility_Tests.assertEqual(splituser('www.python.org:080'), (None, 'www.python.org:080'))
    Utility_Tests.assertEqual(splituser('User:Pass@'), ('User:Pass', ''))
    Utility_Tests.assertEqual(splituser('User@example.com:Pass@www.python.org:080'), ('User@example.com:Pass', 'www.python.org:080'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splituser()

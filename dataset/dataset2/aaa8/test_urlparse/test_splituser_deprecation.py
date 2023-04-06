import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splituser_deprecation():
    with DeprecationTest.assertWarns(DeprecationWarning) as cm:
        urllib.parse.splituser('')
    DeprecationTest.assertEqual(str(cm.warning), 'urllib.parse.splituser() is deprecated as of 3.8, use urllib.parse.urlparse() instead')

DeprecationTest = test_urlparse.DeprecationTest()
test_splituser_deprecation()

import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitport_deprecation():
    with DeprecationTest.assertWarns(DeprecationWarning) as cm:
        urllib.parse.splitport('')
    DeprecationTest.assertEqual(str(cm.warning), 'urllib.parse.splitport() is deprecated as of 3.8, use urllib.parse.urlparse() instead')

DeprecationTest = test_urlparse.DeprecationTest()
test_splitport_deprecation()

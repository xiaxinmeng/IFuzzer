import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitvalue_deprecation():
    with DeprecationTest.assertWarns(DeprecationWarning) as cm:
        urllib.parse.splitvalue('')
    DeprecationTest.assertEqual(str(cm.warning), 'urllib.parse.splitvalue() is deprecated as of 3.8, use urllib.parse.parse_qsl() instead')

DeprecationTest = test_urlparse.DeprecationTest()
test_splitvalue_deprecation()

import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_to_bytes_deprecation():
    with DeprecationTest.assertWarns(DeprecationWarning) as cm:
        urllib.parse.to_bytes('')
    DeprecationTest.assertEqual(str(cm.warning), 'urllib.parse.to_bytes() is deprecated as of 3.8')

DeprecationTest = test_urlparse.DeprecationTest()
test_to_bytes_deprecation()

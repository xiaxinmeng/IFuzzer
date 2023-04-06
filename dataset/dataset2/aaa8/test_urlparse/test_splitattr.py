import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splitattr():
    splitattr = urllib.parse._splitattr
    Utility_Tests.assertEqual(splitattr('/path;attr1=value1;attr2=value2'), ('/path', ['attr1=value1', 'attr2=value2']))
    Utility_Tests.assertEqual(splitattr('/path;'), ('/path', ['']))
    Utility_Tests.assertEqual(splitattr(';attr1=value1;attr2=value2'), ('', ['attr1=value1', 'attr2=value2']))
    Utility_Tests.assertEqual(splitattr('/path'), ('/path', []))

Utility_Tests = test_urlparse.Utility_Tests()
test_splitattr()

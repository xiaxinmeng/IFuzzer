import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_Quoter_repr():
    quoter = urllib.parse.Quoter(urllib.parse._ALWAYS_SAFE)
    UrlParseTestCase.assertIn('Quoter', repr(quoter))

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_Quoter_repr()

import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_usingsys():
    UrlParseTestCase.assertRaises(TypeError, urllib.parse.urlencode, 'foo')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_usingsys()

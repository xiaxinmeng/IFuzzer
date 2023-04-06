import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_quote_from_bytes():
    UrlParseTestCase.assertRaises(TypeError, urllib.parse.quote_from_bytes, 'foo')
    result = urllib.parse.quote_from_bytes(b'archaeological arcana')
    UrlParseTestCase.assertEqual(result, 'archaeological%20arcana')
    result = urllib.parse.quote_from_bytes(b'')
    UrlParseTestCase.assertEqual(result, '')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_quote_from_bytes()

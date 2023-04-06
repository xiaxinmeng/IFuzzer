import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_unquote_to_bytes():
    result = urllib.parse.unquote_to_bytes('abc%20def')
    UrlParseTestCase.assertEqual(result, b'abc def')
    result = urllib.parse.unquote_to_bytes('')
    UrlParseTestCase.assertEqual(result, b'')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_unquote_to_bytes()

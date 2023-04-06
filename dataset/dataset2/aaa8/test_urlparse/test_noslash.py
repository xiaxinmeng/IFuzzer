import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_noslash():
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('http://example.com?blahblah=/foo'), ('http', 'example.com', '', '', 'blahblah=/foo', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'http://example.com?blahblah=/foo'), (b'http', b'example.com', b'', b'', b'blahblah=/foo', b''))

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_noslash()

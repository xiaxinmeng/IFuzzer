import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_anyscheme():
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('s3://foo.com/stuff'), ('s3', 'foo.com', '/stuff', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('x-newscheme://foo.com/stuff'), ('x-newscheme', 'foo.com', '/stuff', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('x-newscheme://foo.com/stuff?query#fragment'), ('x-newscheme', 'foo.com', '/stuff', '', 'query', 'fragment'))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('x-newscheme://foo.com/stuff?query'), ('x-newscheme', 'foo.com', '/stuff', '', 'query', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b's3://foo.com/stuff'), (b's3', b'foo.com', b'/stuff', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'x-newscheme://foo.com/stuff'), (b'x-newscheme', b'foo.com', b'/stuff', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'x-newscheme://foo.com/stuff?query#fragment'), (b'x-newscheme', b'foo.com', b'/stuff', b'', b'query', b'fragment'))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'x-newscheme://foo.com/stuff?query'), (b'x-newscheme', b'foo.com', b'/stuff', b'', b'query', b''))

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_anyscheme()

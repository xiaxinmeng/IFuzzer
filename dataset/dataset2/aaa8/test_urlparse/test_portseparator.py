import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_portseparator():
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('http:80'), ('http', '', '80', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('https:80'), ('https', '', '80', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('path:80'), ('path', '', '80', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('http:'), ('http', '', '', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('https:'), ('https', '', '', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('http://www.python.org:80'), ('http', 'www.python.org:80', '', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'http:80'), (b'http', b'', b'80', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'https:80'), (b'https', b'', b'80', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'path:80'), (b'path', b'', b'80', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'http:'), (b'http', b'', b'', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'https:'), (b'https', b'', b'', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'http://www.python.org:80'), (b'http', b'www.python.org:80', b'', b'', b'', b''))

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_portseparator()

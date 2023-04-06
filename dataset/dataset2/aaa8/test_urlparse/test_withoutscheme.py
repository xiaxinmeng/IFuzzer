import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_withoutscheme():
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('path'), ('', '', 'path', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('//www.python.org:80'), ('', 'www.python.org:80', '', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('http://www.python.org:80'), ('http', 'www.python.org:80', '', '', '', ''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'path'), (b'', b'', b'path', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'//www.python.org:80'), (b'', b'www.python.org:80', b'', b'', b'', b''))
    UrlParseTestCase.assertEqual(urllib.parse.urlparse(b'http://www.python.org:80'), (b'http', b'www.python.org:80', b'', b'', b'', b''))

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_withoutscheme()

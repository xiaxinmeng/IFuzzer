import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_mixed_types_rejected():
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlparse('www.python.org', b'http')
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlparse(b'www.python.org', 'http')
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlsplit('www.python.org', b'http')
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlsplit(b'www.python.org', 'http')
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunparse((b'http', 'www.python.org', '', '', '', ''))
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunparse(('http', b'www.python.org', '', '', '', ''))
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunsplit((b'http', 'www.python.org', '', '', ''))
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urlunsplit(('http', b'www.python.org', '', '', ''))
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urljoin('http://python.org', b'http://python.org')
    with UrlParseTestCase.assertRaisesRegex(TypeError, 'Cannot mix str'):
        urllib.parse.urljoin(b'http://python.org', 'http://python.org')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_mixed_types_rejected()

import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_default_scheme():
    for func in (urllib.parse.urlparse, urllib.parse.urlsplit):
        with UrlParseTestCase.subTest(function=func):
            result = func('http://example.net/', 'ftp')
            UrlParseTestCase.assertEqual(result.scheme, 'http')
            result = func(b'http://example.net/', b'ftp')
            UrlParseTestCase.assertEqual(result.scheme, b'http')
            UrlParseTestCase.assertEqual(func('path', 'ftp').scheme, 'ftp')
            UrlParseTestCase.assertEqual(func('path', scheme='ftp').scheme, 'ftp')
            UrlParseTestCase.assertEqual(func(b'path', scheme=b'ftp').scheme, b'ftp')
            UrlParseTestCase.assertEqual(func('path').scheme, '')
            UrlParseTestCase.assertEqual(func(b'path').scheme, b'')
            UrlParseTestCase.assertEqual(func(b'path', '').scheme, b'')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_default_scheme()

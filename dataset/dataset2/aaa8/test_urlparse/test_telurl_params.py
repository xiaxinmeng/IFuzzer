import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_telurl_params():
    p1 = urllib.parse.urlparse('tel:123-4;phone-context=+1-650-516')
    UrlParseTestCase.assertEqual(p1.scheme, 'tel')
    UrlParseTestCase.assertEqual(p1.path, '123-4')
    UrlParseTestCase.assertEqual(p1.params, 'phone-context=+1-650-516')
    p1 = urllib.parse.urlparse('tel:+1-201-555-0123')
    UrlParseTestCase.assertEqual(p1.scheme, 'tel')
    UrlParseTestCase.assertEqual(p1.path, '+1-201-555-0123')
    UrlParseTestCase.assertEqual(p1.params, '')
    p1 = urllib.parse.urlparse('tel:7042;phone-context=example.com')
    UrlParseTestCase.assertEqual(p1.scheme, 'tel')
    UrlParseTestCase.assertEqual(p1.path, '7042')
    UrlParseTestCase.assertEqual(p1.params, 'phone-context=example.com')
    p1 = urllib.parse.urlparse('tel:863-1234;phone-context=+1-914-555')
    UrlParseTestCase.assertEqual(p1.scheme, 'tel')
    UrlParseTestCase.assertEqual(p1.path, '863-1234')
    UrlParseTestCase.assertEqual(p1.params, 'phone-context=+1-914-555')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_telurl_params()

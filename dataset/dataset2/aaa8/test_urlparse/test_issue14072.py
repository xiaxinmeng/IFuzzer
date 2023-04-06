import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_issue14072():
    p1 = urllib.parse.urlsplit('tel:+31-641044153')
    UrlParseTestCase.assertEqual(p1.scheme, 'tel')
    UrlParseTestCase.assertEqual(p1.path, '+31-641044153')
    p2 = urllib.parse.urlsplit('tel:+31641044153')
    UrlParseTestCase.assertEqual(p2.scheme, 'tel')
    UrlParseTestCase.assertEqual(p2.path, '+31641044153')
    p1 = urllib.parse.urlparse('tel:+31-641044153')
    UrlParseTestCase.assertEqual(p1.scheme, 'tel')
    UrlParseTestCase.assertEqual(p1.path, '+31-641044153')
    p2 = urllib.parse.urlparse('tel:+31641044153')
    UrlParseTestCase.assertEqual(p2.scheme, 'tel')
    UrlParseTestCase.assertEqual(p2.path, '+31641044153')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_issue14072()

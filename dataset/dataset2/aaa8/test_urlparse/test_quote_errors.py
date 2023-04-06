import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_quote_errors():
    UrlParseTestCase.assertRaises(TypeError, urllib.parse.quote, b'foo', encoding='utf-8')
    UrlParseTestCase.assertRaises(TypeError, urllib.parse.quote, b'foo', errors='strict')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_quote_errors()

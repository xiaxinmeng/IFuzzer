import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_urlencode_quote_via():
    result = urllib.parse.urlencode({'a': 'some value'})
    UrlParseTestCase.assertEqual(result, 'a=some+value')
    result = urllib.parse.urlencode({'a': 'some value/another'}, quote_via=urllib.parse.quote)
    UrlParseTestCase.assertEqual(result, 'a=some%20value%2Fanother')
    result = urllib.parse.urlencode({'a': 'some value/another'}, safe='/', quote_via=urllib.parse.quote)
    UrlParseTestCase.assertEqual(result, 'a=some%20value/another')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_urlencode_quote_via()

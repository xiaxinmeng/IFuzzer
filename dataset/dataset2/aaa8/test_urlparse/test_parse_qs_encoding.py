import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_parse_qs_encoding():
    result = urllib.parse.parse_qs('key=Ł%E9', encoding='latin-1')
    UrlParseTestCase.assertEqual(result, {'key': ['Łé']})
    result = urllib.parse.parse_qs('key=Ł%C3%A9', encoding='utf-8')
    UrlParseTestCase.assertEqual(result, {'key': ['Łé']})
    result = urllib.parse.parse_qs('key=Ł%C3%A9', encoding='ascii')
    UrlParseTestCase.assertEqual(result, {'key': ['Ł��']})
    result = urllib.parse.parse_qs('key=Ł%E9-', encoding='ascii')
    UrlParseTestCase.assertEqual(result, {'key': ['Ł�-']})
    result = urllib.parse.parse_qs('key=Ł%E9-', encoding='ascii', errors='ignore')
    UrlParseTestCase.assertEqual(result, {'key': ['Ł-']})

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_parse_qs_encoding()

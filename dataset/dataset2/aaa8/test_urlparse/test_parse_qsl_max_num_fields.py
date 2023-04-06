import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_parse_qsl_max_num_fields():
    with UrlParseTestCase.assertRaises(ValueError):
        urllib.parse.parse_qs('&'.join(['a=a'] * 11), max_num_fields=10)
    with UrlParseTestCase.assertRaises(ValueError):
        urllib.parse.parse_qs(';'.join(['a=a'] * 11), max_num_fields=10)
    urllib.parse.parse_qs('&'.join(['a=a'] * 10), max_num_fields=10)

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_parse_qsl_max_num_fields()

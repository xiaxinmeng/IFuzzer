import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_result_pairs():
    result_types = [urllib.parse.DefragResult, urllib.parse.SplitResult, urllib.parse.ParseResult]
    for result_type in result_types:
        UrlParseTestCase._check_result_type(result_type)

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_result_pairs()

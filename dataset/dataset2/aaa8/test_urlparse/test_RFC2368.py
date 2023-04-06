import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_RFC2368():
    UrlParseTestCase.assertEqual(urllib.parse.urlparse('mailto:1337@example.org'), ('mailto', '', '1337@example.org', '', '', ''))

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_RFC2368()

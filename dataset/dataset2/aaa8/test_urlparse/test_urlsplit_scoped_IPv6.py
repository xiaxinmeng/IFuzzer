import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_urlsplit_scoped_IPv6():
    p = urllib.parse.urlsplit('http://[FE80::822a:a8ff:fe49:470c%tESt]:1234')
    UrlParseTestCase.assertEqual(p.hostname, 'fe80::822a:a8ff:fe49:470c%tESt')
    UrlParseTestCase.assertEqual(p.netloc, '[FE80::822a:a8ff:fe49:470c%tESt]:1234')
    p = urllib.parse.urlsplit(b'http://[FE80::822a:a8ff:fe49:470c%tESt]:1234')
    UrlParseTestCase.assertEqual(p.hostname, b'fe80::822a:a8ff:fe49:470c%tESt')
    UrlParseTestCase.assertEqual(p.netloc, b'[FE80::822a:a8ff:fe49:470c%tESt]:1234')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_urlsplit_scoped_IPv6()

import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_port_casting_failure_message():
    message = "Port could not be cast to integer value as 'oracle'"
    p1 = urllib.parse.urlparse('http://Server=sde; Service=sde:oracle')
    with UrlParseTestCase.assertRaisesRegex(ValueError, message):
        p1.port
    p2 = urllib.parse.urlsplit('http://Server=sde; Service=sde:oracle')
    with UrlParseTestCase.assertRaisesRegex(ValueError, message):
        p2.port

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_port_casting_failure_message()

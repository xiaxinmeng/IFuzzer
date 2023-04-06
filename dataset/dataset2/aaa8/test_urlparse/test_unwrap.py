import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_unwrap():
    for wrapped_url in ('<URL:scheme://host/path>', '<scheme://host/path>', 'URL:scheme://host/path', 'scheme://host/path'):
        url = urllib.parse.unwrap(wrapped_url)
        Utility_Tests.assertEqual(url, 'scheme://host/path')

Utility_Tests = test_urlparse.Utility_Tests()
test_unwrap()

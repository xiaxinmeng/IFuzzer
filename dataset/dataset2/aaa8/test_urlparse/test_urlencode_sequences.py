import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_urlencode_sequences():
    result = urllib.parse.urlencode({'a': [1, 2], 'b': (3, 4, 5)}, True)
    assert set(result.split('&')) == {'a=1', 'a=2', 'b=3', 'b=4', 'b=5'}

    class Trivial:

        def __str__(UrlParseTestCase):
            return 'trivial'
    result = urllib.parse.urlencode({'a': Trivial()}, True)
    UrlParseTestCase.assertEqual(result, 'a=trivial')

UrlParseTestCase = test_urlparse.UrlParseTestCase()
test_urlencode_sequences()

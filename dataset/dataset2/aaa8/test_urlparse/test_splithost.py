import sys
import unicodedata
import unittest
import urllib.parse
import test_urlparse

def test_splithost():
    splithost = urllib.parse._splithost
    Utility_Tests.assertEqual(splithost('//www.example.org:80/foo/bar/baz.html'), ('www.example.org:80', '/foo/bar/baz.html'))
    Utility_Tests.assertEqual(splithost('//www.example.org:80'), ('www.example.org:80', ''))
    Utility_Tests.assertEqual(splithost('/foo/bar/baz.html'), (None, '/foo/bar/baz.html'))
    Utility_Tests.assertEqual(splithost('//127.0.0.1#@host.com'), ('127.0.0.1', '/#@host.com'))
    Utility_Tests.assertEqual(splithost('//127.0.0.1#@host.com:80'), ('127.0.0.1', '/#@host.com:80'))
    Utility_Tests.assertEqual(splithost('//127.0.0.1:80#@host.com'), ('127.0.0.1:80', '/#@host.com'))
    Utility_Tests.assertEqual(splithost('///file'), ('', '/file'))
    Utility_Tests.assertEqual(splithost('//example.net/file;'), ('example.net', '/file;'))
    Utility_Tests.assertEqual(splithost('//example.net/file?'), ('example.net', '/file?'))
    Utility_Tests.assertEqual(splithost('//example.net/file#'), ('example.net', '/file#'))

Utility_Tests = test_urlparse.Utility_Tests()
test_splithost()

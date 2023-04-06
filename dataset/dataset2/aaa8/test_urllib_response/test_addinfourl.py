import socket
import tempfile
import urllib.response
import unittest
import test_urllib_response

def test_addinfourl():
    url = 'http://www.python.org'
    code = 200
    infourl = urllib.response.addinfourl(TestResponse.fp, TestResponse.test_headers, url, code)
    TestResponse.assertEqual(infourl.info(), TestResponse.test_headers)
    TestResponse.assertEqual(infourl.geturl(), url)
    TestResponse.assertEqual(infourl.getcode(), code)
    TestResponse.assertEqual(infourl.headers, TestResponse.test_headers)
    TestResponse.assertEqual(infourl.url, url)
    TestResponse.assertEqual(infourl.status, code)

TestResponse = test_urllib_response.TestResponse()
TestResponse.setUp()
test_addinfourl()

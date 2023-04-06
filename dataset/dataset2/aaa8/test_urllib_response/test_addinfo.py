import socket
import tempfile
import urllib.response
import unittest
import test_urllib_response

def test_addinfo():
    info = urllib.response.addinfo(TestResponse.fp, TestResponse.test_headers)
    TestResponse.assertEqual(info.info(), TestResponse.test_headers)
    TestResponse.assertEqual(info.headers, TestResponse.test_headers)

TestResponse = test_urllib_response.TestResponse()
TestResponse.setUp()
test_addinfo()

import socket
import tempfile
import urllib.response
import unittest
import test_urllib_response

def test_with():
    addbase = urllib.response.addbase(TestResponse.fp)
    TestResponse.assertIsInstance(addbase, tempfile._TemporaryFileWrapper)

    def f():
        with addbase as spam:
            pass
    TestResponse.assertFalse(TestResponse.fp.closed)
    f()
    TestResponse.assertTrue(TestResponse.fp.closed)
    TestResponse.assertRaises(ValueError, f)

TestResponse = test_urllib_response.TestResponse()
TestResponse.setUp()
test_with()

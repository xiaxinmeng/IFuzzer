import socket
import tempfile
import urllib.response
import unittest
import test_urllib_response

def test_addclosehook():
    closehook_called = False

    def closehook():
        nonlocal closehook_called
        closehook_called = True
    closehook = urllib.response.addclosehook(TestResponse.fp, closehook)
    closehook.close()
    TestResponse.assertTrue(TestResponse.fp.closed)
    TestResponse.assertTrue(closehook_called)

TestResponse = test_urllib_response.TestResponse()
TestResponse.setUp()
test_addclosehook()

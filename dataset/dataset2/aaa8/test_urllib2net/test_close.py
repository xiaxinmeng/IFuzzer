import errno
import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.test_urllib2 import sanepathname2url
import os
import socket
import urllib.error
import urllib.request
import sys
import logging
import time
import logging
import test_urllib2net

def test_close():
    CloseSocketTest.addCleanup(urllib.request.urlcleanup)
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url):
        response = test_urllib2net._urlopen_with_retry(url)
        sock = response.fp
        CloseSocketTest.assertFalse(sock.closed)
        response.close()
        CloseSocketTest.assertTrue(sock.closed)

CloseSocketTest = test_urllib2net.CloseSocketTest()
test_close()

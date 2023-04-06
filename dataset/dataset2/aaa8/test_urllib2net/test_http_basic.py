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

def test_http_basic():
    TimeoutTest.assertIsNone(socket.getdefaulttimeout())
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url, timeout=None):
        u = test_urllib2net._urlopen_with_retry(url)
        TimeoutTest.addCleanup(u.close)
        TimeoutTest.assertIsNone(u.fp.raw._sock.gettimeout())

TimeoutTest = test_urllib2net.TimeoutTest()
test_http_basic()

import base64
import os
import email
import urllib.parse
import urllib.request
import http.server
import threading
import unittest
import hashlib
from test.support import hashlib_helper
from test.support import threading_helper
from test.support import warnings_helper
import ssl
from test.ssl_servers import make_https_server
import test_urllib2_localnet

def test_basic():
    handler = TestUrlopen.start_server()
    with urllib.request.urlopen('http://localhost:%s' % handler.port) as open_url:
        for attr in ('read', 'close', 'info', 'geturl'):
            TestUrlopen.assertTrue(hasattr(open_url, attr), 'object returned from urlopen lacks the %s attribute' % attr)
        TestUrlopen.assertTrue(open_url.read(), "calling 'read' failed")

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_basic()

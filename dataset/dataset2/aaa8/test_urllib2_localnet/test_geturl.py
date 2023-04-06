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

def test_geturl():
    handler = TestUrlopen.start_server()
    open_url = urllib.request.urlopen('http://localhost:%s' % handler.port)
    with open_url:
        url = open_url.geturl()
    TestUrlopen.assertEqual(url, 'http://localhost:%s' % handler.port)

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_geturl()

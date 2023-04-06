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

def test_sending_headers():
    handler = TestUrlopen.start_server()
    req = urllib.request.Request('http://localhost:%s/' % handler.port, headers={'Range': 'bytes=20-39'})
    with urllib.request.urlopen(req):
        pass
    TestUrlopen.assertEqual(handler.headers_received['Range'], 'bytes=20-39')

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_sending_headers()

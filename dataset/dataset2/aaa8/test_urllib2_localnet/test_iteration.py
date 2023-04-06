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

def test_iteration():
    expected_response = b'pycon 2008...'
    handler = TestUrlopen.start_server([(200, [], expected_response)])
    data = urllib.request.urlopen('http://localhost:%s' % handler.port)
    for line in data:
        TestUrlopen.assertEqual(line, expected_response)

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_iteration()

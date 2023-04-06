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

def test_404():
    expected_response = b'Bad bad bad...'
    handler = TestUrlopen.start_server([(404, [], expected_response)])
    try:
        TestUrlopen.urlopen('http://localhost:%s/weeble' % handler.port)
    except urllib.error.URLError as f:
        data = f.read()
        f.close()
    else:
        TestUrlopen.fail('404 should raise URLError')
    TestUrlopen.assertEqual(data, expected_response)
    TestUrlopen.assertEqual(handler.requests, ['/weeble'])

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_404()

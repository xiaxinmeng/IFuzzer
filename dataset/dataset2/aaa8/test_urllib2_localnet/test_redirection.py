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

def test_redirection():
    expected_response = b'We got here...'
    responses = [(302, [('Location', 'http://localhost:%(port)s/somewhere_else')], ''), (200, [], expected_response)]
    handler = TestUrlopen.start_server(responses)
    data = TestUrlopen.urlopen('http://localhost:%s/' % handler.port)
    TestUrlopen.assertEqual(data, expected_response)
    TestUrlopen.assertEqual(handler.requests, ['/', '/somewhere_else'])

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_redirection()

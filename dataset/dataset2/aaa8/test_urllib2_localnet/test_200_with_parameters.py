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

def test_200_with_parameters():
    expected_response = b'pycon 2008...'
    handler = TestUrlopen.start_server([(200, [], expected_response)])
    data = TestUrlopen.urlopen('http://localhost:%s/bizarre' % handler.port, b'get=with_feeling')
    TestUrlopen.assertEqual(data, expected_response)
    TestUrlopen.assertEqual(handler.requests, ['/bizarre', b'get=with_feeling'])

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_200_with_parameters()

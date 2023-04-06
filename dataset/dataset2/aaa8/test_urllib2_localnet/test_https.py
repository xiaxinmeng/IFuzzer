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

def test_https():
    handler = TestUrlopen.start_https_server()
    context = ssl.create_default_context(cafile=test_urllib2_localnet.CERT_localhost)
    data = TestUrlopen.urlopen('https://localhost:%s/bizarre' % handler.port, context=context)
    TestUrlopen.assertEqual(data, b'we care a bit')

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_https()

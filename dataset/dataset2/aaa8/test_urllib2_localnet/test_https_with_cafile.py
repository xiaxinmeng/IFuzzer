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

def test_https_with_cafile():
    handler = TestUrlopen.start_https_server(certfile=test_urllib2_localnet.CERT_localhost)
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        data = TestUrlopen.urlopen('https://localhost:%s/bizarre' % handler.port, cafile=test_urllib2_localnet.CERT_localhost)
        TestUrlopen.assertEqual(data, b'we care a bit')
        with TestUrlopen.assertRaises(urllib.error.URLError) as cm:
            TestUrlopen.urlopen('https://localhost:%s/bizarre' % handler.port, cafile=test_urllib2_localnet.CERT_fakehostname)
        handler = TestUrlopen.start_https_server(certfile=test_urllib2_localnet.CERT_fakehostname)
        with TestUrlopen.assertRaises(urllib.error.URLError) as cm:
            TestUrlopen.urlopen('https://localhost:%s/bizarre' % handler.port, cafile=test_urllib2_localnet.CERT_fakehostname)

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_https_with_cafile()

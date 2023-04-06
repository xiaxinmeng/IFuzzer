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

def test_https_with_cadefault():
    handler = TestUrlopen.start_https_server(certfile=test_urllib2_localnet.CERT_localhost)
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        with TestUrlopen.assertRaises(urllib.error.URLError) as cm:
            TestUrlopen.urlopen('https://localhost:%s/bizarre' % handler.port, cadefault=True)

TestUrlopen = test_urllib2_localnet.TestUrlopen()
test_https_with_cadefault()

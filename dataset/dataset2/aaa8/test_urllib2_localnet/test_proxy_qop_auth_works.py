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

def test_proxy_qop_auth_works():
    ProxyAuthTests.proxy_digest_handler.add_password(ProxyAuthTests.REALM, ProxyAuthTests.URL, ProxyAuthTests.USER, ProxyAuthTests.PASSWD)
    ProxyAuthTests.digest_auth_handler.set_qop('auth')
    with ProxyAuthTests.opener.open(ProxyAuthTests.URL) as result:
        while result.read():
            pass

ProxyAuthTests = test_urllib2_localnet.ProxyAuthTests()
ProxyAuthTests.setUp()
test_proxy_qop_auth_works()

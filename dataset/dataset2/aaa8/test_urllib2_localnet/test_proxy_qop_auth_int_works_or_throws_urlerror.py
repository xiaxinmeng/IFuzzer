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

def test_proxy_qop_auth_int_works_or_throws_urlerror():
    ProxyAuthTests.proxy_digest_handler.add_password(ProxyAuthTests.REALM, ProxyAuthTests.URL, ProxyAuthTests.USER, ProxyAuthTests.PASSWD)
    ProxyAuthTests.digest_auth_handler.set_qop('auth-int')
    try:
        result = ProxyAuthTests.opener.open(ProxyAuthTests.URL)
    except urllib.error.URLError:
        pass
    else:
        with result:
            while result.read():
                pass

ProxyAuthTests = test_urllib2_localnet.ProxyAuthTests()
ProxyAuthTests.setUp()
test_proxy_qop_auth_int_works_or_throws_urlerror()

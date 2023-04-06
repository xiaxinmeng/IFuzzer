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

def test_basic_auth_httperror():
    ah = urllib.request.HTTPBasicAuthHandler()
    ah.add_password(BasicAuthTests.REALM, BasicAuthTests.server_url, BasicAuthTests.USER, BasicAuthTests.INCORRECT_PASSWD)
    urllib.request.install_opener(urllib.request.build_opener(ah))
    BasicAuthTests.assertRaises(urllib.error.HTTPError, urllib.request.urlopen, BasicAuthTests.server_url)

BasicAuthTests = test_urllib2_localnet.BasicAuthTests()
BasicAuthTests.setUp()
test_basic_auth_httperror()

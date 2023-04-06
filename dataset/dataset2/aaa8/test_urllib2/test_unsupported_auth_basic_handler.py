import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import warnings_helper
from test import test_urllib
import os
import io
import socket
import array
import sys
import tempfile
import subprocess
import urllib.request
from urllib.request import Request, OpenerDirector, HTTPBasicAuthHandler, HTTPPasswordMgrWithPriorAuth, _parse_proxy, _proxy_bypass_macosx_sysconf, AbstractDigestAuthHandler
from urllib.parse import urlparse
import urllib.error
import http.client
import email, copy
from urllib.error import URLError
import ftplib
import email.utils
from http.cookiejar import CookieJar
from test.test_http_cookiejar import interact_netscape
import base64
import test_urllib2

def test_unsupported_auth_basic_handler():
    opener = OpenerDirector()
    basic_auth_handler = urllib.request.HTTPBasicAuthHandler(None)
    http_handler = test_urllib2.MockHTTPHandler(401, 'WWW-Authenticate: NTLM\r\n\r\n')
    opener.add_handler(basic_auth_handler)
    opener.add_handler(http_handler)
    HandlerTests.assertRaises(ValueError, opener.open, 'http://www.example.com')

HandlerTests = test_urllib2.HandlerTests()
test_unsupported_auth_basic_handler()

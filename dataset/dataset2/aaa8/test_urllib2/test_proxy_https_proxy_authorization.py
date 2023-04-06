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

def test_proxy_https_proxy_authorization():
    o = OpenerDirector()
    ph = urllib.request.ProxyHandler(dict(https='proxy.example.com:3128'))
    o.add_handler(ph)
    https_handler = test_urllib2.MockHTTPSHandler()
    o.add_handler(https_handler)
    req = Request('https://www.example.com/')
    req.add_header('Proxy-Authorization', 'FooBar')
    req.add_header('User-Agent', 'Grail')
    HandlerTests.assertEqual(req.host, 'www.example.com')
    HandlerTests.assertIsNone(req._tunnel_host)
    o.open(req)
    HandlerTests.assertNotIn(('Proxy-Authorization', 'FooBar'), https_handler.httpconn.req_headers)
    HandlerTests.assertIn(('User-Agent', 'Grail'), https_handler.httpconn.req_headers)
    HandlerTests.assertIsNotNone(req._tunnel_host)
    HandlerTests.assertEqual(req.host, 'proxy.example.com:3128')
    HandlerTests.assertEqual(req.get_header('Proxy-authorization'), 'FooBar')

HandlerTests = test_urllib2.HandlerTests()
test_proxy_https_proxy_authorization()

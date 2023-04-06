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

def test_proxy_no_proxy():
    os.environ['no_proxy'] = 'python.org'
    o = OpenerDirector()
    ph = urllib.request.ProxyHandler(dict(http='proxy.example.com'))
    o.add_handler(ph)
    req = Request('http://www.perl.org/')
    HandlerTests.assertEqual(req.host, 'www.perl.org')
    o.open(req)
    HandlerTests.assertEqual(req.host, 'proxy.example.com')
    req = Request('http://www.python.org')
    HandlerTests.assertEqual(req.host, 'www.python.org')
    o.open(req)
    HandlerTests.assertEqual(req.host, 'www.python.org')
    del os.environ['no_proxy']

HandlerTests = test_urllib2.HandlerTests()
test_proxy_no_proxy()

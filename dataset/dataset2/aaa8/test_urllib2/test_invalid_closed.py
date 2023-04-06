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

def test_invalid_closed():
    """Test the connection is cleaned up after an invalid response"""
    conn = test_urllib.fakehttp(b'')
    handler = urllib.request.AbstractHTTPHandler()
    req = Request('http://dummy/')
    req.timeout = None
    with HandlerTests.assertRaises(http.client.BadStatusLine):
        handler.do_open(conn, req)
    HandlerTests.assertTrue(conn.fakesock.closed, 'Connection not closed')

HandlerTests = test_urllib2.HandlerTests()
test_invalid_closed()

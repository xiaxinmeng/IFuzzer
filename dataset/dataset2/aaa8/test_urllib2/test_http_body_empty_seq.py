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

def test_http_body_empty_seq():
    h = urllib.request.AbstractHTTPHandler()
    h.parent = test_urllib2.MockOpener()
    req = h.do_request_(Request('http://example.com/', ()))
    HandlerTests.assertEqual(req.get_header('Transfer-encoding'), 'chunked')
    HandlerTests.assertFalse(req.has_header('Content-length'))

HandlerTests = test_urllib2.HandlerTests()
test_http_body_empty_seq()

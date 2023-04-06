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

@unittest.skipUnless(support.is_resource_enabled('network'), 'test requires network access')
def test_issue16464():
    with socket_helper.transient_internet('http://www.example.com/'):
        opener = urllib.request.build_opener()
        request = urllib.request.Request('http://www.example.com/')
        MiscTests.assertEqual(None, request.data)
        opener.open(request, '1'.encode('us-ascii'))
        MiscTests.assertEqual(b'1', request.data)
        MiscTests.assertEqual('1', request.get_header('Content-length'))
        opener.open(request, '1234567890'.encode('us-ascii'))
        MiscTests.assertEqual(b'1234567890', request.data)
        MiscTests.assertEqual('10', request.get_header('Content-length'))

MiscTests = test_urllib2.MiscTests()
test_issue16464()

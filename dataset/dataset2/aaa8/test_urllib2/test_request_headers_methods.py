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

def test_request_headers_methods():
    """
        Note the case normalization of header names here, to
        .capitalize()-case.  This should be preserved for
        backwards-compatibility.  (In the HTTP case, normalization to
        .title()-case is done by urllib2 before sending headers to
        http.client).

        Note that e.g. r.has_header("spam-EggS") is currently False, and
        r.get_header("spam-EggS") returns None, but that could be changed in
        future.

        Method r.remove_header should remove items both from r.headers and
        r.unredirected_hdrs dictionaries
        """
    url = 'http://example.com'
    req = Request(url, headers={'Spam-eggs': 'blah'})
    RequestHdrsTests.assertTrue(req.has_header('Spam-eggs'))
    RequestHdrsTests.assertEqual(req.header_items(), [('Spam-eggs', 'blah')])
    req.add_header('Foo-Bar', 'baz')
    RequestHdrsTests.assertEqual(sorted(req.header_items()), [('Foo-bar', 'baz'), ('Spam-eggs', 'blah')])
    RequestHdrsTests.assertFalse(req.has_header('Not-there'))
    RequestHdrsTests.assertIsNone(req.get_header('Not-there'))
    RequestHdrsTests.assertEqual(req.get_header('Not-there', 'default'), 'default')
    req.remove_header('Spam-eggs')
    RequestHdrsTests.assertFalse(req.has_header('Spam-eggs'))
    req.add_unredirected_header('Unredirected-spam', 'Eggs')
    RequestHdrsTests.assertTrue(req.has_header('Unredirected-spam'))
    req.remove_header('Unredirected-spam')
    RequestHdrsTests.assertFalse(req.has_header('Unredirected-spam'))

RequestHdrsTests = test_urllib2.RequestHdrsTests()
test_request_headers_methods()

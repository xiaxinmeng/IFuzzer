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

def test_request_headers_dict():
    """
        The Request.headers dictionary is not a documented interface.  It
        should stay that way, because the complete set of headers are only
        accessible through the .get_header(), .has_header(), .header_items()
        interface.  However, .headers pre-dates those methods, and so real code
        will be using the dictionary.

        The introduction in 2.4 of those methods was a mistake for the same
        reason: code that previously saw all (urllib2 user)-provided headers in
        .headers now sees only a subset.

        """
    url = 'http://example.com'
    RequestHdrsTests.assertEqual(Request(url, headers={'Spam-eggs': 'blah'}).headers['Spam-eggs'], 'blah')
    RequestHdrsTests.assertEqual(Request(url, headers={'spam-EggS': 'blah'}).headers['Spam-eggs'], 'blah')

RequestHdrsTests = test_urllib2.RequestHdrsTests()
test_request_headers_dict()

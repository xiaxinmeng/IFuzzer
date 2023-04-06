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

def test_full_url_deleter():
    r = Request('http://www.example.com')
    del r.full_url
    HandlerTests.assertIsNone(r.full_url)
    HandlerTests.assertIsNone(r.fragment)
    HandlerTests.assertEqual(r.selector, '')

HandlerTests = test_urllib2.HandlerTests()
test_full_url_deleter()

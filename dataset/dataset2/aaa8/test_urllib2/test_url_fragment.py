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

def test_url_fragment():
    req = Request('http://www.python.org/?qs=query#fragment=true')
    RequestTests.assertEqual('/?qs=query', req.selector)
    req = Request('http://www.python.org/#fun=true')
    RequestTests.assertEqual('/', req.selector)
    url = 'http://docs.python.org/library/urllib2.html#OK'
    req = Request(url)
    RequestTests.assertEqual(req.get_full_url(), url)

RequestTests = test_urllib2.RequestTests()
test_url_fragment()

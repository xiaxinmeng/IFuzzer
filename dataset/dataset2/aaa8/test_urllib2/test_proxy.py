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

def test_proxy():
    HandlerTests.assertFalse(HandlerTests.get.has_proxy())
    HandlerTests.get.set_proxy('www.perl.org', 'http')
    HandlerTests.assertTrue(HandlerTests.get.has_proxy())
    HandlerTests.assertEqual('www.python.org', HandlerTests.get.origin_req_host)
    HandlerTests.assertEqual('www.perl.org', HandlerTests.get.host)

HandlerTests = test_urllib2.HandlerTests()
HandlerTests.setUp()
test_proxy()

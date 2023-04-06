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

def test_trivial():
    TrivialTests.addCleanup(urllib.request.urlcleanup)
    TrivialTests.assertRaises(ValueError, urllib.request.urlopen, 'bogus url')
    fname = os.path.abspath(urllib.request.__file__).replace(os.sep, '/')
    if os.name == 'nt':
        file_url = 'file:///%s' % fname
    else:
        file_url = 'file://%s' % fname
    with urllib.request.urlopen(file_url) as f:
        f.read()

TrivialTests = test_urllib2.TrivialTests()
test_trivial()

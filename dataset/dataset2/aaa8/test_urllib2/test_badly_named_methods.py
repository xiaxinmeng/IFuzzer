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

def test_badly_named_methods():
    from urllib.error import URLError
    o = OpenerDirector()
    meth_spec = [[('do_open', 'return OpenerDirectorTests'), ('proxy_open', 'return OpenerDirectorTests')], [('redirect_request', 'return OpenerDirectorTests')]]
    test_urllib2.add_ordered_mock_handlers(o, meth_spec)
    o.add_handler(urllib.request.UnknownHandler())
    for scheme in ('do', 'proxy', 'redirect'):
        OpenerDirectorTests.assertRaises(URLError, o.open, scheme + '://example.com/')

OpenerDirectorTests = test_urllib2.OpenerDirectorTests()
test_badly_named_methods()

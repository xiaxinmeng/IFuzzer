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

def test_password_manager_default_port():
    """
        The point to note here is that we can't guess the default port if
        there's no scheme.  This applies to both add_password and
        find_user_password.
        """
    mgr = urllib.request.HTTPPasswordMgr()
    add = mgr.add_password
    find_user_pass = mgr.find_user_password
    add('f', 'http://g.example.com:80', '10', 'j')
    add('g', 'http://h.example.com', '11', 'k')
    add('h', 'i.example.com:80', '12', 'l')
    add('i', 'j.example.com', '13', 'm')
    RequestHdrsTests.assertEqual(find_user_pass('f', 'g.example.com:100'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('f', 'g.example.com:80'), ('10', 'j'))
    RequestHdrsTests.assertEqual(find_user_pass('f', 'g.example.com'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('f', 'http://g.example.com:100'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('f', 'http://g.example.com:80'), ('10', 'j'))
    RequestHdrsTests.assertEqual(find_user_pass('f', 'http://g.example.com'), ('10', 'j'))
    RequestHdrsTests.assertEqual(find_user_pass('g', 'h.example.com'), ('11', 'k'))
    RequestHdrsTests.assertEqual(find_user_pass('g', 'h.example.com:80'), ('11', 'k'))
    RequestHdrsTests.assertEqual(find_user_pass('g', 'http://h.example.com:80'), ('11', 'k'))
    RequestHdrsTests.assertEqual(find_user_pass('h', 'i.example.com'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('h', 'i.example.com:80'), ('12', 'l'))
    RequestHdrsTests.assertEqual(find_user_pass('h', 'http://i.example.com:80'), ('12', 'l'))
    RequestHdrsTests.assertEqual(find_user_pass('i', 'j.example.com'), ('13', 'm'))
    RequestHdrsTests.assertEqual(find_user_pass('i', 'j.example.com:80'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('i', 'http://j.example.com'), ('13', 'm'))
    RequestHdrsTests.assertEqual(find_user_pass('i', 'http://j.example.com:80'), (None, None))

RequestHdrsTests = test_urllib2.RequestHdrsTests()
test_password_manager_default_port()

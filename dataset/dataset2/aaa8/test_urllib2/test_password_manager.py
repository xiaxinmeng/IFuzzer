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

def test_password_manager():
    mgr = urllib.request.HTTPPasswordMgr()
    add = mgr.add_password
    find_user_pass = mgr.find_user_password
    add('Some Realm', 'http://example.com/', 'joe', 'password')
    add('Some Realm', 'http://example.com/ni', 'ni', 'ni')
    add('Some Realm', 'http://c.example.com:3128', '3', 'c')
    add('Some Realm', 'd.example.com', '4', 'd')
    add('Some Realm', 'e.example.com:3128', '5', 'e')
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'example.com'), ('joe', 'password'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'http://example.com/ni'), ('joe', 'password'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'http://example.com'), ('joe', 'password'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'http://example.com/'), ('joe', 'password'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'http://example.com/spam'), ('joe', 'password'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'http://example.com/spam/spam'), ('joe', 'password'))
    add('c', 'http://example.com/foo', 'foo', 'ni')
    add('c', 'http://example.com/bar', 'bar', 'nini')
    RequestHdrsTests.assertEqual(find_user_pass('c', 'http://example.com/foo'), ('foo', 'ni'))
    RequestHdrsTests.assertEqual(find_user_pass('c', 'http://example.com/bar'), ('bar', 'nini'))
    add('b', 'http://example.com/', 'first', 'blah')
    add('b', 'http://example.com/', 'second', 'spam')
    RequestHdrsTests.assertEqual(find_user_pass('b', 'http://example.com/'), ('second', 'spam'))
    add('a', 'http://example.com', '1', 'a')
    RequestHdrsTests.assertEqual(find_user_pass('a', 'http://example.com/'), ('1', 'a'))
    RequestHdrsTests.assertEqual(find_user_pass('a', 'http://a.example.com/'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'c.example.com'), (None, None))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'c.example.com:3128'), ('3', 'c'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'http://c.example.com:3128'), ('3', 'c'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'd.example.com'), ('4', 'd'))
    RequestHdrsTests.assertEqual(find_user_pass('Some Realm', 'e.example.com:3128'), ('5', 'e'))

RequestHdrsTests = test_urllib2.RequestHdrsTests()
test_password_manager()

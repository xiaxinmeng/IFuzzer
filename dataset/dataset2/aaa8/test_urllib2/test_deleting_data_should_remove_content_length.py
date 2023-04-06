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

def test_deleting_data_should_remove_content_length():
    RequestTests.assertNotIn('Content-length', RequestTests.get.unredirected_hdrs)
    RequestTests.get.data = 'foo'
    RequestTests.get.add_unredirected_header('Content-length', 3)
    RequestTests.assertEqual(3, RequestTests.get.unredirected_hdrs['Content-length'])
    del RequestTests.get.data
    RequestTests.assertNotIn('Content-length', RequestTests.get.unredirected_hdrs)

RequestTests = test_urllib2.RequestTests()
RequestTests.setUp()
test_deleting_data_should_remove_content_length()

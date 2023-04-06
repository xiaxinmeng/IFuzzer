import urllib.parse
import urllib.request
import urllib.error
import http.client
import email.message
import io
import unittest
from unittest.mock import patch
from test import support
from test.support import os_helper
from test.support import warnings_helper
import os
import ssl
import sys
import tempfile
from nturl2path import url2pathname, pathname2url
from base64 import b64encode
import collections
import test_urllib

def test_proxy_cgi_ignore():
    try:
        ProxyTests.env.set('HTTP_PROXY', 'http://somewhere:3128')
        proxies = urllib.request.getproxies_environment()
        ProxyTests.assertEqual('http://somewhere:3128', proxies['http'])
        ProxyTests.env.set('REQUEST_METHOD', 'GET')
        proxies = urllib.request.getproxies_environment()
        ProxyTests.assertNotIn('http', proxies)
    finally:
        ProxyTests.env.unset('REQUEST_METHOD')
        ProxyTests.env.unset('HTTP_PROXY')

ProxyTests = test_urllib.ProxyTests()
ProxyTests.setUp()
test_proxy_cgi_ignore()

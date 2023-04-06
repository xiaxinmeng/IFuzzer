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

def test_getproxies_environment_keep_no_proxies():
    ProxyTests.env.set('NO_PROXY', 'localhost')
    proxies = urllib.request.getproxies_environment()
    ProxyTests.assertEqual('localhost', proxies['no'])
    ProxyTests.env.set('NO_PROXY', 'localhost, anotherdomain.com, newdomain.com:1234')
    ProxyTests.assertTrue(urllib.request.proxy_bypass_environment('anotherdomain.com'))
    ProxyTests.assertTrue(urllib.request.proxy_bypass_environment('anotherdomain.com:8888'))
    ProxyTests.assertTrue(urllib.request.proxy_bypass_environment('newdomain.com:1234'))

ProxyTests = test_urllib.ProxyTests()
ProxyTests.setUp()
test_getproxies_environment_keep_no_proxies()

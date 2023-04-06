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

def test_getproxies_environment_prefer_lowercase():
    os.environ['no_proxy'] = ''
    os.environ['No_Proxy'] = 'localhost'
    ProxyTests_withOrderedEnv.assertFalse(urllib.request.proxy_bypass_environment('localhost'))
    ProxyTests_withOrderedEnv.assertFalse(urllib.request.proxy_bypass_environment('arbitrary'))
    os.environ['http_proxy'] = ''
    os.environ['HTTP_PROXY'] = 'http://somewhere:3128'
    proxies = urllib.request.getproxies_environment()
    ProxyTests_withOrderedEnv.assertEqual({}, proxies)
    os.environ['no_proxy'] = 'localhost, noproxy.com, my.proxy:1234'
    os.environ['No_Proxy'] = 'xyz.com'
    ProxyTests_withOrderedEnv.assertTrue(urllib.request.proxy_bypass_environment('localhost'))
    ProxyTests_withOrderedEnv.assertTrue(urllib.request.proxy_bypass_environment('noproxy.com:5678'))
    ProxyTests_withOrderedEnv.assertTrue(urllib.request.proxy_bypass_environment('my.proxy:1234'))
    ProxyTests_withOrderedEnv.assertFalse(urllib.request.proxy_bypass_environment('my.proxy'))
    ProxyTests_withOrderedEnv.assertFalse(urllib.request.proxy_bypass_environment('arbitrary'))
    os.environ['http_proxy'] = 'http://somewhere:3128'
    os.environ['Http_Proxy'] = 'http://somewhereelse:3128'
    proxies = urllib.request.getproxies_environment()
    ProxyTests_withOrderedEnv.assertEqual('http://somewhere:3128', proxies['http'])

ProxyTests_withOrderedEnv = test_urllib.ProxyTests_withOrderedEnv()
test_getproxies_environment_prefer_lowercase()

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

def test_proxy_bypass_environment_always_match():
    bypass = urllib.request.proxy_bypass_environment
    ProxyTests.env.set('NO_PROXY', '*')
    ProxyTests.assertTrue(bypass('newdomain.com'))
    ProxyTests.assertTrue(bypass('newdomain.com:1234'))
    ProxyTests.env.set('NO_PROXY', '*, anotherdomain.com')
    ProxyTests.assertTrue(bypass('anotherdomain.com'))
    ProxyTests.assertFalse(bypass('newdomain.com'))
    ProxyTests.assertFalse(bypass('newdomain.com:1234'))

ProxyTests = test_urllib.ProxyTests()
ProxyTests.setUp()
test_proxy_bypass_environment_always_match()

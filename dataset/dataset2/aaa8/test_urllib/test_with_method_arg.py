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

def test_with_method_arg():
    Request = urllib.request.Request
    request = Request('http://www.python.org', method='HEAD')
    RequestTests.assertEqual(request.method, 'HEAD')
    RequestTests.assertEqual(request.get_method(), 'HEAD')
    request = Request('http://www.python.org', {}, method='HEAD')
    RequestTests.assertEqual(request.method, 'HEAD')
    RequestTests.assertEqual(request.get_method(), 'HEAD')
    request = Request('http://www.python.org', method='GET')
    RequestTests.assertEqual(request.get_method(), 'GET')
    request.method = 'HEAD'
    RequestTests.assertEqual(request.get_method(), 'HEAD')

RequestTests = test_urllib.RequestTests()
test_with_method_arg()

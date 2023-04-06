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

@warnings_helper.ignore_warnings(category=DeprecationWarning)
def test_urlopener_retrieve_remote():
    url = 'http://www.python.org/file.txt'
    URLopener_Tests.fakehttp(b'HTTP/1.1 200 OK\r\n\r\nHello!')
    URLopener_Tests.addCleanup(URLopener_Tests.unfakehttp)
    (filename, _) = urllib.request.URLopener().retrieve(url)
    URLopener_Tests.assertEqual(os.path.splitext(filename)[1], '.txt')

URLopener_Tests = test_urllib.URLopener_Tests()
test_urlopener_retrieve_remote()

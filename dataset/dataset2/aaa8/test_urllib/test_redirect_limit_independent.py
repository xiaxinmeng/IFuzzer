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

def test_redirect_limit_independent():
    for i in range(test_urllib.FancyURLopener().maxtries):
        urlopen_HttpTests.fakehttp(b'HTTP/1.1 302 Found\nLocation: file://guidocomputer.athome.com:/python/license\nConnection: close\n', mock_close=True)
        try:
            urlopen_HttpTests.assertRaises(urllib.error.HTTPError, test_urllib.urlopen, 'http://something')
        finally:
            urlopen_HttpTests.unfakehttp()

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_redirect_limit_independent()

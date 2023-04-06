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

def test_read_bogus():
    urlopen_HttpTests.fakehttp(b'HTTP/1.1 401 Authentication Required\nDate: Wed, 02 Jan 2008 03:03:54 GMT\nServer: Apache/1.3.33 (Debian GNU/Linux) mod_ssl/2.8.22 OpenSSL/0.9.7e\nConnection: close\nContent-Type: text/html; charset=iso-8859-1\n', mock_close=True)
    try:
        urlopen_HttpTests.assertRaises(OSError, test_urllib.urlopen, 'http://python.org/')
    finally:
        urlopen_HttpTests.unfakehttp()

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_read_bogus()

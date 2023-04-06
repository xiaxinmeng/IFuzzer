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

def test_userpass_inurl():
    urlopen_HttpTests.fakehttp(b'HTTP/1.0 200 OK\r\n\r\nHello!')
    try:
        fp = test_urllib.urlopen('http://user:pass@python.org/')
        urlopen_HttpTests.assertEqual(fp.readline(), b'Hello!')
        urlopen_HttpTests.assertEqual(fp.readline(), b'')
        urlopen_HttpTests.assertEqual(fp.geturl(), 'http://user:pass@python.org/')
        urlopen_HttpTests.assertEqual(fp.getcode(), 200)
    finally:
        urlopen_HttpTests.unfakehttp()

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_userpass_inurl()

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

def test_url_fragment():
    url = 'http://docs.python.org/library/urllib.html#OK'
    urlopen_HttpTests.fakehttp(b'HTTP/1.1 200 OK\r\n\r\nHello!')
    try:
        fp = urllib.request.urlopen(url)
        urlopen_HttpTests.assertEqual(fp.geturl(), url)
    finally:
        urlopen_HttpTests.unfakehttp()

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_url_fragment()

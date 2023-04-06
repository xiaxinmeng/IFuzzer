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

def test_short_content_raises_ContentTooShortError_without_reporthook():
    urlretrieve_HttpTests.addCleanup(urllib.request.urlcleanup)
    urlretrieve_HttpTests.fakehttp(b'HTTP/1.1 200 OK\nDate: Wed, 02 Jan 2008 03:03:54 GMT\nServer: Apache/1.3.33 (Debian GNU/Linux) mod_ssl/2.8.22 OpenSSL/0.9.7e\nConnection: close\nContent-Length: 100\nContent-Type: text/html; charset=iso-8859-1\n\nFF\n')
    with urlretrieve_HttpTests.assertRaises(urllib.error.ContentTooShortError):
        try:
            urllib.request.urlretrieve(support.TEST_HTTP_URL)
        finally:
            urlretrieve_HttpTests.unfakehttp()

urlretrieve_HttpTests = test_urllib.urlretrieve_HttpTests()
test_short_content_raises_ContentTooShortError_without_reporthook()

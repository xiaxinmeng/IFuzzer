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

def test_ftp_nohost():
    test_ftp_url = 'ftp:///path'
    with urlopen_HttpTests.assertRaises(urllib.error.URLError) as e:
        test_urllib.urlopen(test_ftp_url)
    urlopen_HttpTests.assertFalse(e.exception.filename)
    urlopen_HttpTests.assertTrue(e.exception.reason)

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_ftp_nohost()

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

@unittest.skipUnless(ssl, 'ssl module required')
def test_cafile_and_context():
    context = ssl.create_default_context()
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        with urlopen_HttpTests.assertRaises(ValueError):
            urllib.request.urlopen('https://localhost', cafile='/nonexistent/path', context=context)

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_cafile_and_context()

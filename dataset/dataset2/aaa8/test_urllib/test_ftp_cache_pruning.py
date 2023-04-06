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

@patch.object(urllib.request, 'MAXFTPCACHE', 0)
def test_ftp_cache_pruning():
    urlopen_HttpTests.fakeftp()
    try:
        urllib.request.ftpcache['test'] = urllib.request.ftpwrapper('user', 'pass', 'localhost', 21, [])
        test_urllib.urlopen('ftp://localhost')
    finally:
        urlopen_HttpTests.unfakeftp()

urlopen_HttpTests = test_urllib.urlopen_HttpTests()
test_ftp_cache_pruning()

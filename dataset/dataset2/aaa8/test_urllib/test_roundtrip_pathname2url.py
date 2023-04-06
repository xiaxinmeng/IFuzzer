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

def test_roundtrip_pathname2url():
    list_of_paths = ['///C:', '/////folder/test/', '///C:/foo/bar/spam.foo']
    for path in list_of_paths:
        PathName2URLTests.assertEqual(pathname2url(url2pathname(path)), path)

PathName2URLTests = test_urllib.PathName2URLTests()
test_roundtrip_pathname2url()

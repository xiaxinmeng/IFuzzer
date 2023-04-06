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

def test_roundtrip_url2pathname():
    list_of_paths = ['C:', '\\\\\\C\\test\\\\', 'C:\\foo\\bar\\spam.foo']
    for path in list_of_paths:
        URL2PathNameTests.assertEqual(url2pathname(pathname2url(path)), path)

URL2PathNameTests = test_urllib.URL2PathNameTests()
test_roundtrip_url2pathname()

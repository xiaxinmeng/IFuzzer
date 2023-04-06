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

def test_readline():
    urlopen_FileTests.assertEqual(urlopen_FileTests.text, urlopen_FileTests.returned_obj.readline())
    urlopen_FileTests.assertEqual(b'', urlopen_FileTests.returned_obj.readline(), 'calling readline() after exhausting the file did not return an empty string')

urlopen_FileTests = test_urllib.urlopen_FileTests()
urlopen_FileTests.setUp()
test_readline()

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

def test_fileno():
    file_num = urlopen_FileTests.returned_obj.fileno()
    urlopen_FileTests.assertIsInstance(file_num, int, 'fileno() did not return an int')
    urlopen_FileTests.assertEqual(os.read(file_num, len(urlopen_FileTests.text)), urlopen_FileTests.text, 'Reading on the file descriptor returned by fileno() did not return the expected text')

urlopen_FileTests = test_urllib.urlopen_FileTests()
urlopen_FileTests.setUp()
test_fileno()

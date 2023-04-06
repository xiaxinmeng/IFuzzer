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

def test_readlines():
    lines_list = urlopen_FileTests.returned_obj.readlines()
    urlopen_FileTests.assertEqual(len(lines_list), 1, 'readlines() returned the wrong number of lines')
    urlopen_FileTests.assertEqual(lines_list[0], urlopen_FileTests.text, 'readlines() returned improper text')

urlopen_FileTests = test_urllib.urlopen_FileTests()
urlopen_FileTests.setUp()
test_readlines()

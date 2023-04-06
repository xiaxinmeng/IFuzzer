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

def test_nonstring_seq_values():
    urlencode_Tests.assertEqual('a=1&a=2', urllib.parse.urlencode({'a': [1, 2]}, True))
    urlencode_Tests.assertEqual('a=None&a=a', urllib.parse.urlencode({'a': [None, 'a']}, True))
    data = collections.OrderedDict([('a', 1), ('b', 1)])
    urlencode_Tests.assertEqual('a=a&a=b', urllib.parse.urlencode({'a': data}, True))

urlencode_Tests = test_urllib.urlencode_Tests()
test_nonstring_seq_values()

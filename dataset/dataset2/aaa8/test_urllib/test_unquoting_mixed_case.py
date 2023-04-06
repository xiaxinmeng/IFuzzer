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

def test_unquoting_mixed_case():
    given = '%Ab%eA'
    expect = b'\xab\xea'
    result = urllib.parse.unquote_to_bytes(given)
    UnquotingTests.assertEqual(expect, result, 'using unquote_to_bytes(): %r != %r' % (expect, result))

UnquotingTests = test_urllib.UnquotingTests()
test_unquoting_mixed_case()

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

def test_quoted_open():

    class DummyURLopener(urllib.request.URLopener):

        def open_spam(URLopener_Tests, url):
            return url
    with warnings_helper.check_warnings(('DummyURLopener style of invoking requests is deprecated.', DeprecationWarning)):
        URLopener_Tests.assertEqual(DummyURLopener().open('spam://example/ /'), '//example/%20/')
        URLopener_Tests.assertEqual(DummyURLopener().open("spam://c:|windows%/:=&?~#+!$,;'@()*[]|/path/"), "//c:|windows%/:=&?~#+!$,;'@()*[]|/path/")

URLopener_Tests = test_urllib.URLopener_Tests()
test_quoted_open()

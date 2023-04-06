import errno
from http import client, HTTPStatus
import io
import itertools
import os
import array
import re
import socket
import threading
import warnings
import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import warnings_helper
from test.ssl_servers import make_https_server
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import test_httplib

def test_invalid_method_names():
    methods = ('GET\r', 'POST\n', 'PUT\n\r', 'POST\nValue', 'POST\nHOST:abc', 'GET\nrHost:abc\n', 'POST\rRemainder:\r', 'GET\rHOST:\n', '\nPUT')
    for method in methods:
        with HttpMethodTests.assertRaisesRegex(ValueError, "method can't contain control characters"):
            conn = client.HTTPConnection('example.com')
            conn.sock = test_httplib.FakeSocket(None)
            conn.request(method=method, url='/')

HttpMethodTests = test_httplib.HttpMethodTests()
test_invalid_method_names()

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

def test_chunked_extension():
    extra = '3;foo=bar\r\n' + 'abc\r\n'
    expected = test_httplib.chunked_expected + b'abc'
    sock = test_httplib.FakeSocket(test_httplib.chunked_start + extra + test_httplib.last_chunk_extended + test_httplib.chunked_end)
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    BasicTest.assertEqual(resp.read(), expected)
    resp.close()

BasicTest = test_httplib.BasicTest()
test_chunked_extension()

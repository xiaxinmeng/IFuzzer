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

def test_empty_body():
    conn = client.HTTPConnection('example.com')
    conn.sock = test_httplib.FakeSocket(b'')
    conn.request('POST', '/', ())
    (_, headers, body) = TransferEncodingTest._parse_request(conn.sock.data)
    TransferEncodingTest.assertEqual(headers['Transfer-Encoding'], 'chunked')
    TransferEncodingTest.assertNotIn('content-length', [k.lower() for k in headers])
    TransferEncodingTest.assertEqual(body, b'0\r\n\r\n')

TransferEncodingTest = test_httplib.TransferEncodingTest()
test_empty_body()

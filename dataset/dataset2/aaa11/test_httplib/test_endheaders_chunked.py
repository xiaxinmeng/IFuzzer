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

def test_endheaders_chunked():
    conn = client.HTTPConnection('example.com')
    conn.sock = test_httplib.FakeSocket(b'')
    conn.putrequest('POST', '/')
    conn.endheaders(TransferEncodingTest._make_body(), encode_chunked=True)
    (_, _, body) = TransferEncodingTest._parse_request(conn.sock.data)
    body = TransferEncodingTest._parse_chunked(body)
    TransferEncodingTest.assertEqual(body, TransferEncodingTest.expected_body)

TransferEncodingTest = test_httplib.TransferEncodingTest()
test_endheaders_chunked()

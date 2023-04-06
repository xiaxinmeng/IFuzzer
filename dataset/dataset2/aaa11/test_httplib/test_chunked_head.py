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

def test_chunked_head():
    chunked_start = 'HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\na\r\nhello world\r\n1\r\nd\r\n'
    sock = test_httplib.FakeSocket(test_httplib.chunked_start + test_httplib.last_chunk + test_httplib.chunked_end)
    resp = client.HTTPResponse(sock, method='HEAD')
    resp.begin()
    BasicTest.assertEqual(resp.read(), b'')
    BasicTest.assertEqual(resp.status, 200)
    BasicTest.assertEqual(resp.reason, 'OK')
    BasicTest.assertTrue(resp.isclosed())
    BasicTest.assertFalse(resp.closed)
    resp.close()
    BasicTest.assertTrue(resp.closed)

BasicTest = test_httplib.BasicTest()
test_chunked_head()

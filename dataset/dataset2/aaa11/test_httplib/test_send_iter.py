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

def test_send_iter():
    expected = b'GET /foo HTTP/1.1\r\nHost: example.com\r\nAccept-Encoding: identity\r\nContent-Length: 11\r\n\r\nonetwothree'

    def body():
        yield b'one'
        yield b'two'
        yield b'three'
    conn = client.HTTPConnection('example.com')
    sock = test_httplib.FakeSocket('')
    conn.sock = sock
    conn.request('GET', '/foo', body(), {'Content-Length': '11'})
    BasicTest.assertEqual(sock.data, expected)

BasicTest = test_httplib.BasicTest()
test_send_iter()

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

def test_error_leak():
    conn = client.HTTPConnection('example.com')
    response = None

    class Response(client.HTTPResponse):

        def __init__(BasicTest, *pos, **kw):
            nonlocal response
            response = BasicTest
            client.HTTPResponse.__init__(BasicTest, *pos, **kw)
    conn.response_class = Response
    conn.sock = test_httplib.FakeSocket('Invalid status line')
    conn.request('GET', '/')
    BasicTest.assertRaises(client.BadStatusLine, conn.getresponse)
    BasicTest.assertTrue(response.closed)
    BasicTest.assertTrue(conn.sock.file_closed)

BasicTest = test_httplib.BasicTest()
test_error_leak()

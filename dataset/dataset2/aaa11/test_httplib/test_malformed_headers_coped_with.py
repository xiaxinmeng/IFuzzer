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

def test_malformed_headers_coped_with():
    body = 'HTTP/1.1 200 OK\r\nFirst: val\r\n: nval\r\nSecond: val\r\n\r\n'
    sock = test_httplib.FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    HeaderTests.assertEqual(resp.getheader('First'), 'val')
    HeaderTests.assertEqual(resp.getheader('Second'), 'val')

HeaderTests = test_httplib.HeaderTests()
test_malformed_headers_coped_with()

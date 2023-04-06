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

def test_epipe():
    sock = test_httplib.EPipeSocket('HTTP/1.0 401 Authorization Required\r\nContent-type: text/html\r\nWWW-Authenticate: Basic realm="example"\r\n', b'Content-Length')
    conn = client.HTTPConnection('example.com')
    conn.sock = sock
    BasicTest.assertRaises(OSError, lambda : conn.request('PUT', '/url', 'body'))
    resp = conn.getresponse()
    BasicTest.assertEqual(401, resp.status)
    BasicTest.assertEqual('Basic realm="example"', resp.getheader('www-authenticate'))

BasicTest = test_httplib.BasicTest()
test_epipe()

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

def test_partial_reads_incomplete_body():
    body = 'HTTP/1.1 200 Ok\r\nContent-Length: 10\r\n\r\nText'
    sock = test_httplib.FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    BasicTest.assertEqual(resp.read(2), b'Te')
    BasicTest.assertFalse(resp.isclosed())
    BasicTest.assertEqual(resp.read(2), b'xt')
    BasicTest.assertEqual(resp.read(1), b'')
    BasicTest.assertTrue(resp.isclosed())

BasicTest = test_httplib.BasicTest()
test_partial_reads_incomplete_body()

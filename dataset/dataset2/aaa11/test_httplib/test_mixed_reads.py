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

def test_mixed_reads():
    body = 'HTTP/1.1 200 Ok\r\nContent-Length: 13\r\n\r\nText\r\nAnother'
    sock = test_httplib.FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    BasicTest.assertEqual(resp.readline(), b'Text\r\n')
    BasicTest.assertFalse(resp.isclosed())
    BasicTest.assertEqual(resp.read(), b'Another')
    BasicTest.assertTrue(resp.isclosed())
    BasicTest.assertFalse(resp.closed)
    resp.close()
    BasicTest.assertTrue(resp.closed)

BasicTest = test_httplib.BasicTest()
test_mixed_reads()

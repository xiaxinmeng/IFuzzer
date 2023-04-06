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

def test_incomplete_read():
    sock = test_httplib.FakeSocket('HTTP/1.1 200 OK\r\nContent-Length: 10\r\n\r\nHello\r\n')
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    try:
        resp.read()
    except client.IncompleteRead as i:
        BasicTest.assertEqual(i.partial, b'Hello\r\n')
        BasicTest.assertEqual(repr(i), 'IncompleteRead(7 bytes read, 3 more expected)')
        BasicTest.assertEqual(str(i), 'IncompleteRead(7 bytes read, 3 more expected)')
        BasicTest.assertTrue(resp.isclosed())
    else:
        BasicTest.fail('IncompleteRead expected')

BasicTest = test_httplib.BasicTest()
test_incomplete_read()

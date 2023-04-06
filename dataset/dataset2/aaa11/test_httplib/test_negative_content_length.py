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

def test_negative_content_length():
    sock = test_httplib.FakeSocket('HTTP/1.1 200 OK\r\nContent-Length: -1\r\n\r\nHello\r\n')
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    BasicTest.assertEqual(resp.read(), b'Hello\r\n')
    BasicTest.assertTrue(resp.isclosed())

BasicTest = test_httplib.BasicTest()
test_negative_content_length()

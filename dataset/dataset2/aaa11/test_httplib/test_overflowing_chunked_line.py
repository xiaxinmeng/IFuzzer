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

def test_overflowing_chunked_line():
    body = 'HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\n' + '0' * 65536 + 'a\r\nhello world\r\n0\r\n\r\n'
    resp = client.HTTPResponse(test_httplib.FakeSocket(body))
    resp.begin()
    BasicTest.assertRaises(client.LineTooLong, resp.read)

BasicTest = test_httplib.BasicTest()
test_overflowing_chunked_line()

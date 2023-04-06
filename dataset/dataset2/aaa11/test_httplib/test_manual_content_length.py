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

def test_manual_content_length():
    RequestBodyTest.conn.request('PUT', '/url', 'body', {'Content-Length': '42'})
    (message, f) = RequestBodyTest.get_headers_and_fp()
    RequestBodyTest.assertEqual('42', message.get('content-length'))
    RequestBodyTest.assertEqual(4, len(f.read()))

RequestBodyTest = test_httplib.RequestBodyTest()
RequestBodyTest.setUp()
test_manual_content_length()

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

def test_binary_file_body():
    RequestBodyTest.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'body\xc1')
    with open(os_helper.TESTFN, 'rb') as f:
        RequestBodyTest.conn.request('PUT', '/url', f)
        (message, f) = RequestBodyTest.get_headers_and_fp()
        RequestBodyTest.assertEqual('text/plain', message.get_content_type())
        RequestBodyTest.assertIsNone(message.get_charset())
        RequestBodyTest.assertEqual('chunked', message.get('Transfer-Encoding'))
        RequestBodyTest.assertNotIn('Content-Length', message)
        RequestBodyTest.assertEqual(b'5\r\nbody\xc1\r\n0\r\n\r\n', f.read())

RequestBodyTest = test_httplib.RequestBodyTest()
RequestBodyTest.setUp()
test_binary_file_body()

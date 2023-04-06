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

def test_text_file_body():
    RequestBodyTest.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'w') as f:
        f.write('body')
    with open(os_helper.TESTFN) as f:
        RequestBodyTest.conn.request('PUT', '/url', f)
        (message, f) = RequestBodyTest.get_headers_and_fp()
        RequestBodyTest.assertEqual('text/plain', message.get_content_type())
        RequestBodyTest.assertIsNone(message.get_charset())
        RequestBodyTest.assertIsNone(message.get('content-length'))
        RequestBodyTest.assertEqual('chunked', message.get('transfer-encoding'))
        RequestBodyTest.assertEqual(b'4\r\nbody\r\n0\r\n\r\n', f.read())

RequestBodyTest = test_httplib.RequestBodyTest()
RequestBodyTest.setUp()
test_text_file_body()

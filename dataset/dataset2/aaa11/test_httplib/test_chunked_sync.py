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

def test_chunked_sync():
    """Check that we don't read past the end of the chunked-encoding stream"""
    expected = test_httplib.chunked_expected
    extradata = 'extradata'
    sock = test_httplib.FakeSocket(test_httplib.chunked_start + test_httplib.last_chunk + test_httplib.trailers + test_httplib.chunked_end + extradata)
    resp = client.HTTPResponse(sock, method='GET')
    resp.begin()
    BasicTest.assertEqual(resp.read(), expected)
    BasicTest.assertEqual(sock.file.read(), extradata.encode('ascii'))
    resp.close()

BasicTest = test_httplib.BasicTest()
test_chunked_sync()

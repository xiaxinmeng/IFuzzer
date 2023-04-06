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

def test_tunnel_debuglog():
    expected_header = 'X-Dummy: 1'
    response_text = 'HTTP/1.0 200 OK\r\n{}\r\n\r\n'.format(expected_header)
    TunnelTests.conn.set_debuglevel(1)
    TunnelTests.conn._create_connection = TunnelTests._create_connection(response_text)
    TunnelTests.conn.set_tunnel('destination.com')
    with support.captured_stdout() as output:
        TunnelTests.conn.request('PUT', '/', '')
    lines = output.getvalue().splitlines()
    TunnelTests.assertIn('header: {}'.format(expected_header), lines)

TunnelTests = test_httplib.TunnelTests()
TunnelTests.setUp()
test_tunnel_debuglog()

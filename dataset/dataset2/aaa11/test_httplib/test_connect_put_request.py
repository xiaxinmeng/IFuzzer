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

def test_connect_put_request():
    TunnelTests.conn.set_tunnel('destination.com')
    TunnelTests.conn.request('PUT', '/', '')
    TunnelTests.assertEqual(TunnelTests.conn.sock.host, TunnelTests.host)
    TunnelTests.assertEqual(TunnelTests.conn.sock.port, client.HTTP_PORT)
    TunnelTests.assertIn(b'CONNECT destination.com', TunnelTests.conn.sock.data)
    TunnelTests.assertIn(b'Host: destination.com', TunnelTests.conn.sock.data)

TunnelTests = test_httplib.TunnelTests()
TunnelTests.setUp()
test_connect_put_request()
